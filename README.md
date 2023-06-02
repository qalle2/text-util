# text-util
Simple command-line text-processing utilities in Python.

Table of contents:
* [Line-oriented](#line-oriented)
* [Other](#other)

## Line-oriented

### asciify.py
Read lines from stdin. Replace Latin non-ASCII letters with closest equivalent ASCII letters using Python's unicodedata.decomposition() and a custom replacement table.

### casefold.py
Print lines from stdin in a format suitable for caseless comparisons.

### countlines.py
Print unique lines and their counts from stdin.

### findword.py
```
Search the Unix dictionary case-insensitively. For playing word games.
Words with characters other than A-Z or a-z won't be searched.
Arguments: WORD SOMEWHERE NOWHERE
    WORD:      a word with hyphens (-) in place of unknown letters; required
    SOMEWHERE: letters that occur somewhere in the word; optional;
               use hyphen (-) for none if you don't want to set this argument
               but want to set the next argument
    NOWHERE:   letters that don't occur in the word; optional
Examples:
    CH---- EO RS
        will find six-letter words that start with CH and contain E and O
        but no R or S (e.g. CHOICE).
    ---TH - EI
        will find five-letter words that end with TH and don't contain E or I
        (e.g. CLOTH)
```

### findword2.py
Suggest words to begin a Mastermind-style game with. Arguments: word length, optionally a list of letters (a-z) to ignore.

Example:
```
$ python3 findword2.py 4
Words (no more than 10):
ARES (score=3920)
EARS (score=3920)
ERAS (score=3920)
SEAR (score=3920)
SERA (score=3920)
ALES (score=3913)
ELSA (score=3913)
LASE (score=3913)
LEAS (score=3913)
LESA (score=3913)
```

### finsort.py
Print lines from stdin in case-insensitive Finnish order. See [Jukka Korpela: Nykyajan kielenopas &ndash; Aakkosjärjestys](http://www.jkorpela.fi/kielenopas/4.15.html) (in Finnish).

### grouplines.py
Group lines from stdin by prefix (LENGTH > 0), suffix (LENGTH &lt; 0) or entire line (LENGTH = 0). Print number of lines in each group. Argument: LENGTH

### lineset.py
Print setwise union (OPERATION=u), intersection (OPERATION=i) or difference (OPERATION=d) of lines without duplicates. Args: OPERATION FILE1 [FILE2 ...]

### rus_iso9.py
Romanize Russian (Cyrillic) text from stdin using the ISO 9 romanization. See [Wikipedia: Venäjän translitterointi &ndash; ISO 9](https://fi.wikipedia.org/wiki/Ven%C3%A4j%C3%A4n_translitterointi#ISO_9) (in Finnish).

### uniquelines.py
Print unique lines from stdin.

## Other

### countchars.py
Print codepoints, names and counts of unique characters from stdin.

### getwords.py
Print words (sequences of Unicode Letter characters or non-initial non-final apostrophes) from stdin.
