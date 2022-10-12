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
Find a word in the Unix dictionary case-insensitively. No characters other than
a-z allowed. For Mastermind-style word games.
Arguments:
    - required: a word; use '-' in place of an unknown letter
    - optional: letters that occur somewhere in the word; '-' = none
    - optional: letters that do not occur anywhere in the word
Examples:
    chu---       6-letter words that start with 'chu'
    ---th ro     5-letter words that end with 'th' and contain 'r' and 'o'
    ---th ro f   5-letter words that end with 'th' and contain 'r' and 'o' but
                 not 'f'
    v--- - e     4-letter words that start with 'v' and don't contain 'e'
```

Example:
```
$ python3 findword.py st--- ro e
Words that match specified pattern:
    STORK
    STORM
    STORY
    STROP
Unknown letters: K M P Y
Words with many common unknown letters:
    AMPLY (score=3)
    BUMPY (score=3)
    CAMPY (score=3)
    DUMPY (score=3)
    EMPTY (score=3)
    GIMPY (score=3)
    IMPLY (score=3)
    JUMPY (score=3)
    LUMPY (score=3)
    LYMPH (score=3)
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
