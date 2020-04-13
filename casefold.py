"""Copy stdin to stdout and fold the letter case (using Python's str.casefold() method)."""

import sys

def main():
    """The main function."""

    for line in sys.stdin:
        print((line[:-1] if line.endswith("\n") else line).casefold())

if __name__ == "__main__":
    main()
