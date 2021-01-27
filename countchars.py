"""Print codepoints, names and counts of unique characters from stdin."""

import collections
import sys
import unicodedata

def main():
    chars = collections.Counter()
    for line in sys.stdin:
        chars.update(line[:-1] if line.endswith("\n") else line)

    for char in chars:
        name = unicodedata.name(char, "?")
        print(f'{ord(char)},"{name}",{chars[char]}')

if __name__ == "__main__":
    main()
