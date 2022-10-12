# print lines from stdin in a format suitable for caseless comparisons

import sys

for line in sys.stdin:
    print(line.rstrip("\n").casefold())
