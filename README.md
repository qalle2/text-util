# simple-util
Some simple command-line utilities in Python.

## casefold.py
```
Copy stdin to stdout and fold the letter case (using Python's str.casefold() method).
```

## count_words.py
```
usage: count_words.py [-h] [-c]

Count words (sequences of Unicode Letter characters) from stdin. Output distinct words and their counts in CSV format
in Unicode order.

optional arguments:
  -h, --help       show this help message and exit
  -c, --no-counts  Do not print the word counts.
```

Hint: use the output from casefold.py as input to this program.

## md5.py
```
Compute the MD5 hash of a file. Argument: filename
```

Just a UI for Python's `hashlib.md5()`.

## pygrep.py
```
Print lines from stdin that match a regular expression case-insensitively. Argument: regular expression
```

Just a UI for Python's `re.search()`.

## split.py
```
usage: split.py [-h] input_file part_size output_pattern

Split a file.

positional arguments:
  input_file      the file to read (size: PART_SIZE + 1 to 1000 * PART_SIZE)
  part_size       the size of each output file in bytes (1 or more; the last file may be smaller)
  output_pattern  the pattern for output files; must include exactly one asterisk ("*"); the asterisk will be replaced
                  with 1-3 digits depending on how many files will be output

optional arguments:
  -h, --help      show this help message and exit
```
