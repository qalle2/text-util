# print words (sequences of Unicode Letter characters or non-initial non-final
# apostrophes) from stdin

import sys, unicodedata

APOSTROPHES = "'’"

for line in sys.stdin:
    startPos = None  # start position of current word
    line = line + " "  # must end with a non-letter non-apostrophe character

    for (pos, char) in enumerate(line):
        isLetter = unicodedata.category(char).startswith("L")
        if startPos is None and isLetter:
            # start a word
            startPos = pos
        elif startPos is not None and not isLetter and char not in APOSTROPHES:
            # end a word
            print(line[startPos:pos].rstrip(APOSTROPHES))
            startPos = None
