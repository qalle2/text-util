"""Count Unicode codepoints in a text file."""

import argparse
import collections
import os
import sys
import unicodedata

def parse_arguments():
    """Parse command line arguments using argparse."""

    parser = argparse.ArgumentParser(
        description="Count Unicode codepoints in a text file. Output them in CSV format, sorted by "
        "codepoint.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="See https://unicode.org/reports/tr44/#Property_Values for general category values."
    )

    parser.add_argument(
        "-n", "--normalization", choices=("", "nfd", "nfc", "nfkd", "nfkc"), default="",
        help="Which Unicode Normalization Form to apply to each line (\"\"=none). See "
        "https://unicode.org/reports/tr15/#Norm_Forms"
    )
    parser.add_argument("input_file", help="The UTF-8 text file to read.")

    args = parser.parse_args()
    if not os.path.isfile(args.input_file):
        sys.exit("Input file not found.")
    return args

def count_codepoints(handle, settings):
    """Count codepoints in the file."""

    handle.seek(0)
    codepointCounts = collections.Counter()
    for line in handle:
        if settings.normalization:
            line = unicodedata.normalize(settings.normalization.upper(), line)
        codepointCounts.update(ord(char) for char in line)
    return codepointCounts

def print_codepoints(codepointCounts):
    """Print codepoints in CSV format."""

    print('"codepoint","name","general category","count"')
    for codepoint in sorted(codepointCounts):
        char = chr(codepoint)
        print('{:d},"{:s}","{:s}",{:d}'.format(
            codepoint,
            unicodedata.name(char, "(unknown)"),
            unicodedata.category(char),
            codepointCounts[codepoint]
        ))

def main():
    """The main function."""

    settings = parse_arguments()
    try:
        with open(settings.input_file, "rt", encoding="utf8") as handle:
            codepointCounts = count_codepoints(handle, settings)
    except UnicodeDecodeError:
        sys.exit("Error: the file is not a UTF-8 text file.")
    except OSError:
        sys.exit("Error reading the file.")
    print_codepoints(codepointCounts)

if __name__ == "__main__":
    main()
