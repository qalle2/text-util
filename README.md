# simple-util
Some simple command-line text-processing utilities in Python. All the programs read from stdin and write to stdout.

## casefold.py
Fold the letter case (using Python's [``str.casefold()``](https://docs.python.org/3/library/stdtypes.html#str.casefold) method).

## count_codepoints.py
Count Unicode codepoints and output them in CSV format, sorted by codepoint.

## count_words.py
Count words (sequences of Unicode Letter characters). Output distinct words and their counts in CSV format in Unicode order.

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

