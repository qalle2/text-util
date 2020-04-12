# simple-util
Some simple utilities in Python.

## md5.py
Compute the MD5 hash of a file. Just a UI for Python's hashlib.

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
