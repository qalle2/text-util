# text-util
Simple command-line text-processing utilities in Python.

## Line-oriented

### casefold.py
Print lines from stdin via Python's .casefold() method.

### countlines.py
Print unique lines and their counts from stdin.

### finsort.py
Print lines from stdin in case-insensitive Finnish order. See http://www.jkorpela.fi/kielenopas/4.15.html

### grouplines.py
Group lines from stdin by prefix (LENGTH > 0), suffix (LENGTH < 0) or entire line (LENGTH = 0). Print number of lines in each group. Argument: LENGTH

### lineset.py
Print setwise union (OPERATION=u), intersection (OPERATION=i) or difference (OPERATION=d) of lines without duplicates. Args: OPERATION FILE1 [FILE2 ...]

### uniquelines.py
Print unique lines from stdin.

## Other

### countchars.py
Print codepoints, names and counts of unique characters from stdin.

### getwords.py
Print words (sequences of Unicode Letter characters or non-initial non-final apostrophes) from stdin.
