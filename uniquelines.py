"""Print unique lines from stdin."""

import sys

for line in set(l.rstrip("\n") for l in sys.stdin):
    print(line)
