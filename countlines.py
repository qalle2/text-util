"""Print unique lines and their counts from stdin."""

import collections, sys

for (line, count) in collections.Counter(l.rstrip("\n") for l in sys.stdin).items():
    print(f'"{line}",{count}')
