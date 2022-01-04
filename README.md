# text-util
Simple command-line text-processing utilities in Python.

## Line-oriented

### asciify.py
Read lines from stdin. Replace Latin non-ASCII letters with closest equivalent ASCII letters using Python's unicodedata.decomposition() and a custom replacement table.

### casefold.py
Print lines from stdin via Python's .casefold() method.

### countlines.py
Print unique lines and their counts from stdin.

### findword.py
```
Find a word in the Unix dictionary case-insensitively. No characters other than a-z allowed.
For Mastermind-style word games.
Arguments (first one only, first and second one or all three):
    - a word; hyphen ('-') = unknown letter
    - letters that occur somewhere in the word; hyphen ('-') = none
    - letters that do not occur anywhere in the word
Examples:
    chu---       six-letter  words that start with 'chu'
    ---th ro     five-letter words that end   with 'th' and contain 'r' and 'o'
    ---th ro f   five-letter words that end   with 'th' and contain 'r' and 'o' but no 'f'
    v--- - e     four-letter words that start with 'v'  and don't contain 'e'
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
