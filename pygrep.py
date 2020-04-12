"""Print lines from stdin that match a regular expression."""

import re
import sys

def main():
    """The main function."""

    if len(sys.argv) != 2:
        sys.exit(
            "Print lines from stdin that match a regular expression case-insensitively. Argument: "
            "regular expression"
        )

    try:
        regex = re.compile(sys.argv[1], re.IGNORECASE)
    except re.error as e:
        sys.exit("Error: " + str(e))

    for line in sys.stdin:
        line = line[:-1] if line.endswith("\n") else line
        if regex.search(line) is not None:
            print(line)

if __name__ == "__main__":
    main()
