"""Print unique lines and their counts from stdin."""

import collections, sys

lineCounts = collections.Counter(l.rstrip("\n") for l in sys.stdin)

for line in lineCounts:
    print(f'"{line}",{lineCounts[line]}')
