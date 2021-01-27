# text-util
Simple command-line text-processing utilities in Python.

## casefold.py
Print lines from stdin via Python's [``.casefold()``](https://docs.python.org/library/stdtypes.html#str.casefold) method.

## countchars.py
Print codepoints, names and counts of unique characters from stdin.

## countlines.py
Print unique lines and their counts from stdin.

## getwords.py
Print words (sequences of Unicode Letter characters) from stdin.

## lineset.py
Read one or more text files. Print the setwise union, intersection or difference of the lines without duplicates.

Command line arguments: *operation* *files*
* *operation*: `u`=union (lines in any file), `i`=intersection (lines in all files), `d`=difference (lines in the first but no other files)
* *files*: one or more UTF-8 text files

## uniquelines.py
Print unique lines from stdin.
