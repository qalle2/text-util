"""Count words (sequences of Unicode Letter characters) from stdin. Output distinct words and their
counts in CSV format in Unicode order."""

import collections
import sys
import unicodedata

def string_to_words(string_):
    """Generate words (sequences of Unicode Letter characters) from a string."""

    wordStartPos = None
    for (pos, char) in enumerate(string_):
        isLetter = unicodedata.category(char).startswith("L")
        if wordStartPos is None and isLetter:
            # start a word
            wordStartPos = pos
        elif wordStartPos is not None and not isLetter:
            # end a word
            yield string_[wordStartPos:pos]
            wordStartPos = None
    if wordStartPos is not None:
        # end the last word
        yield string_[wordStartPos:]

def stdin_to_words():
    """Generate words from stdin."""

    for line in sys.stdin:
        for word in string_to_words(line):
            yield word

def main():
    """The main function."""

    words = dict(collections.Counter(stdin_to_words()))
    for word in sorted(words):
        print(f'"{word:s}",{words[word]:d}')

if __name__ == "__main__":
    main()
