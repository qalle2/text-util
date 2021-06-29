"""Print lines from stdin via Python's .casefold() method."""

import sys

for line in sys.stdin:
    print(line.rstrip("\n").casefold())
