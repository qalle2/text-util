"""Print unique lines and their counts from stdin."""

import collections
import sys

def main():
    words = collections.Counter(
        line[:-1] if line.endswith("\n") else line for line in sys.stdin
    )
    for word in words:
        print(f'"{word:s}",{words[word]}')

if __name__ == "__main__":
    main()
