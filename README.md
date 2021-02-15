# text-util
Simple command-line text-processing utilities in Python.

## Line-oriented

### casefold.py
Print lines from stdin via Python's [``.casefold()``](https://docs.python.org/library/stdtypes.html#str.casefold) method.

### countlines.py
Print unique lines and their counts from stdin.

### finsort.py
Print lines (with duplicates) from stdin in case-insensitive Finnish order.

### grouplines.py
Group lines from stdin by prefix (LENGTH > 0), suffix (LENGTH < 0) or entire line (LENGTH = 0). Print number of lines in each group. Argument: LENGTH

### lineset.py
Read one or more text files. Print the setwise union, intersection or difference of the lines without duplicates.

Command line arguments: *operation* *files*
* *operation*: `u`=union (lines in any file), `i`=intersection (lines in all files), `d`=difference (lines in the first but no other files)
* *files*: one or more UTF-8 text files

### uniquelines.py
Print unique lines from stdin.

## Other

### countchars.py
Print codepoints, names and counts of unique characters from stdin.

### getwords.py
Print words (sequences of Unicode Letter characters) from stdin.
