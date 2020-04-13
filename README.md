# simple-util
Some simple command-line utilities in Python.

## casefold.py
Copy stdin to stdout and fold the letter case (using Python's str.casefold() method).

## count_codepoints.py
Count Unicode codepoints from stdin. Output them in CSV format, sorted by codepoint.

Hint: use the output from casefold.py or uninorm.py as input to this program.

## count_words.py
Count words (sequences of Unicode Letter characters) from stdin. Output distinct words and their counts in CSV format in Unicode order.

Hint: use the output from casefold.py or uninorm.py as input to this program.

## md5.py
Compute the MD5 hash of a file. Argument: filename

Just a UI for Python's `hashlib.md5()`.

## pygrep.py
Print lines from stdin that match a regular expression case-insensitively. Argument: regular expression

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

## uninorm.py
```
usage: uninorm.py [-h] [-n {nfd,nfc,nfkd,nfkc}]

Copy stdin to stdout and apply one of the Unicode Normalization Forms.

optional arguments:
  -h, --help            show this help message and exit
  -n {nfd,nfc,nfkd,nfkc}, --normalization {nfd,nfc,nfkd,nfkc}
                        Which Unicode Normalization Form to apply to each line. See
                        https://unicode.org/reports/tr15/#Norm_Forms (default: nfc)
```

Just a UI for Python's `unicodedata.normalize()`.
