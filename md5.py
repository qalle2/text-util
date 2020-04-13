"""Compute the MD5 hash of a file."""

import hashlib
import os
import sys

def read_file(handle):
    """Read a file. Yield one chunk per call."""

    bytesLeft = handle.seek(0, 2)
    handle.seek(0)
    while bytesLeft:
        chunkSize = min(bytesLeft, 2 ** 20)
        yield handle.read(chunkSize)
        bytesLeft -= chunkSize

def main():
    """The main function."""

    if len(sys.argv) != 2:
        sys.exit("Compute the MD5 hash of a file. Argument: filename")
    file = sys.argv[1]
    if not os.path.isfile(file):
        sys.exit("File not found.")

    hash_ = hashlib.md5()
    try:
        with open(file, "rb") as handle:
            for chunk in read_file(handle):
                hash_.update(chunk)
    except OSError:
        sys.exit("Error reading the file.")
    print(hash_.hexdigest(), os.path.basename(file))

if __name__ == "__main__":
    main()
