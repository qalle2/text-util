"""Print codepoints, names and counts of unique characters from stdin."""

import collections, sys, unicodedata

charCounts = collections.Counter()
for line in sys.stdin:
    charCounts.update(line.rstrip("\n"))

for char in charCounts:
    name = unicodedata.name(char, "?")
    print(f'{ord(char)},"{name}",{charCounts[char]}')
