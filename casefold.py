"""Print lines from stdin via Python's .casefold() method."""

import sys

def main():
    for line in sys.stdin:
        print((line[:-1] if line.endswith("\n") else line).casefold())

if __name__ == "__main__":
    main()
