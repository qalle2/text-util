"""Print words (sequences of Unicode Letter characters) from stdin."""

import sys
import unicodedata

def get_words(string_):
    wordStartPos = None
    for (pos, char) in enumerate(string_):
        isLetter = unicodedata.category(char).startswith("L")
        if wordStartPos is None and isLetter:
            # start word
            wordStartPos = pos
        elif wordStartPos is not None and not isLetter:
            # end word
            yield string_[wordStartPos:pos]
            wordStartPos = None
    if wordStartPos is not None:
        # end word
        yield string_[wordStartPos:]

def main():
    for line in sys.stdin:
        for word in get_words(line):
            print(word)

if __name__ == "__main__":
    main()
