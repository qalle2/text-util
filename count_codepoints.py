"""Count Unicode codepoints from stdin. Output them in CSV format, sorted by codepoint.
See https://unicode.org/reports/tr44/#Property_Values for Unicode general category values."""

import collections
import sys
import unicodedata

def count_characters_from_stdin():
    """Count characters from stdin."""

    chars = collections.Counter()
    for line in sys.stdin:
        line = line[:-1] if line.endswith("\n") else line
        chars.update(char for char in line)
    return chars

def main():
    """The main function."""

    chars = count_characters_from_stdin()
    print('"codepoint","name","general category","count"')
    for char in sorted(chars):
        print('{:d},"{:s}","{:s}",{:d}'.format(
            ord(char),
            unicodedata.name(char, "(unknown)"),
            unicodedata.category(char),
            chars[char]
        ))

if __name__ == "__main__":
    main()
