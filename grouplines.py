"""Read lines from stdin, print number of each distinct prefix/suffix."""

import collections
import sys

def get_substrings(length):
    """Generate prefixes/suffixes of specified length from stdin."""

    for line in sys.stdin:
        line = line.rstrip("\n")
        yield line[:length] if length > 0 else line[length:]

def main():
    if len(sys.argv) != 2:
        sys.exit(
            "Read lines from stdin. Group them by prefix (LENGTH > 0), suffix (LENGTH < 0) or "
            "whole line (LENGTH = 0). Print number of lines in each group. Argument: LENGTH"
        )

    try:
        length = int(sys.argv[1], 10)
    except ValueError:
        sys.exit("LENGTH must be an integer.")

    # count prefixes/suffixes/whole lines
    counts = collections.Counter(get_substrings(length))

    # sort first by descending count, then alphabetically (case-insensitively)
    substrs = sorted(counts)
    substrs.sort(key=lambda s: s.casefold())
    substrs.sort(key=lambda s: counts[s], reverse=True)

    # print counts
    formatCode = ("<" if length > 0 else ">") + str(abs(length) + 2) + "s"
    for substr in substrs:
        substr2 = format(f'"{substr}"', formatCode)
        print(f"{substr2}: {counts[substr]}")

if __name__ == "__main__":
    main()
