import collections, itertools, re, os, string, sys

HELP_TEXT = """\
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
        (e.g. CLOTH)\
"""

DICT_PATHS = (
    "/etc/dictionaries-common/words",
    "/usr/dict/words",
    "/usr/share/dict/words",
)

def parse_args():
    # return (string word, set somewhere, set nowhere)

    if not 2 <= len(sys.argv) <= 4:
        sys.exit(HELP_TEXT)

    word = sys.argv[1].upper()
    if len(sys.argv) >= 3 and sys.argv[2] != "-":
        somewhere = set(sys.argv[2].upper())
    else:
        somewhere = set()
    if len(sys.argv) >= 4:
        nowhere = set(sys.argv[3].upper())
    else:
        nowhere = set()

    if re.search("^[A-Z-]+$", word) is None:
        sys.exit("Invalid WORD argument.")
    if somewhere - set(string.ascii_uppercase):
        sys.exit("Invalid SOMEWHERE argument.")
    if nowhere - set(string.ascii_uppercase):
        sys.exit("Invalid NOWHERE argument.")

    if len(somewhere) > word.count("-"):
        sys.exit(
            "There can't be more letters in SOMEWHERE argument than there are "
            "hyphens in WORD."
        )

    if set(word) & (somewhere | nowhere) or somewhere & nowhere:
        sys.exit("No two arguments can contain the same letters.")

    return (word, somewhere, nowhere)

def get_words(length):
    # generate words of specified length in upper case

    try:
        dictPath = [f for f in DICT_PATHS if os.path.exists(f)][0]
    except IndexError:
        sys.exit("Unix dictionary file not found.")

    regex = re.compile("^[A-Za-z]{" + str(length) + "}$")

    try:
        with open(dictPath, "rt") as handle:
            handle.seek(0)
            yield from (
                w.rstrip("\n").upper() for w in handle
                if regex.search(w) is not None
            )
    except OSError:
        sys.exit("Error reading file.")

def filter_words(words, arg1, arg2, arg3):
    # generate user-specified words
    regex = re.compile(
        "^" + "".join(c if c != "-" else "." for c in arg1) + "$",
        re.IGNORECASE
    )
    yield from (
        w for w in words
        if regex.search(w) is not None
        and arg2.issubset(set(w)) and arg3.isdisjoint(set(w))
    )

def main():
    (arg1, arg2, arg3) = parse_args()

    words = set(get_words(len(arg1)))
    if not words:
        sys.exit("No words with specified length in dictionary.")

    filteredWords = set(filter_words(words, arg1, arg2, arg3))

    print(f"Words that match specified pattern ({len(filteredWords)}):")
    if set(arg1) == set("-") and not arg2 and not arg3:
        print("(Not shown because the search wasn't narrowed down at all)")
    else:
        for word in sorted(filteredWords):
            print(word)

    # count letters in words that match specified pattern (only once per word)
    letterCnts = collections.Counter(
        itertools.chain.from_iterable(set(w) for w in filteredWords)
    )
    unknownLetters = set(letterCnts) - set(arg1) - arg2 - arg3
    print("Unknown letters:", "".join(sorted(unknownLetters)))

    print("Words with many common unknown letters:")
    scoresByWord = dict(
        (w, sum(letterCnts[l] for l in set(w) & unknownLetters)) for w in words
    )
    suggestions = sorted(w for w in words if scoresByWord[w] > 0)
    suggestions.sort(key=lambda w: scoresByWord[w], reverse=True)
    for word in suggestions[:10]:
        print(f"{word} (score={scoresByWord[word]})")

main()
