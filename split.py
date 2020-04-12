"""Split a file."""

import argparse
import os
import sys

def parse_arguments():
    """Parse command line arguments using argparse."""

    parser = argparse.ArgumentParser(
        description="Split a file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "input_file", help="the file to read (size: PART_SIZE + 1 to 1000 * PART_SIZE)"
    )
    parser.add_argument(
        "part_size", type=int,
        help="the size of each output file in bytes (1 or more; the last file may be smaller)"
    )
    parser.add_argument(
        "output_pattern",
        help="the pattern for output files; must include exactly one asterisk (\"*\"); the "
        "asterisk will be replaced with 1-3 digits depending on how many files will be output"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        sys.exit("Input file not found.")
    if args.part_size < 1:
        sys.exit("Invalid part size.")
    if args.output_pattern.count("*") != 1:
        sys.exit("Invalid output pattern.")

    return args

def read_file(source, bytesLeft):
    """Read a part of a file starting from current position. Yield one chunk per call."""

    while bytesLeft:
        chunkSize = min(bytesLeft, 2 ** 20)
        yield source.read(chunkSize)
        bytesLeft -= chunkSize

def split_file(source, partSize, outputPattern):
    """Split a file."""

    inputFileSize = source.seek(0, 2)
    # get number of parts and digits; for integers, ceil(a / b) == (a + b - 1) // b
    partCount = (inputFileSize + partSize - 1) // partSize
    if not 2 <= partCount <= 1000:
        sys.exit("The splitting must result in 2 to 1000 parts.")
    digitCount = 1 if partCount <= 10 else (2 if partCount <= 100 else 3)
    # split
    numberFormat = "0" + str(digitCount) + "d"
    source.seek(0)
    for part in range(partCount):
        outputFile = outputPattern.replace("*", format(part, numberFormat))
        print(f"Writing {outputFile:s}...")
        if os.path.exists(outputFile):
            sys.exit("File already exists, quitting.")
        with open(outputFile, "wb") as target:
            target.seek(0)
            for chunk in read_file(source, partSize):
                target.write(chunk)

def main():
    """The main function."""

    args = parse_arguments()

    try:
        with open(args.input_file, "rb") as source:
            split_file(source, args.part_size, args.output_pattern)
    except OSError:
        sys.exit("Error reading/writing files.")

if __name__ == "__main__":
    main()
