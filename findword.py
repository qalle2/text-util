import collections, re, os, sys

HELP_TEXT = """\
Find a word in the Unix dictionary case-insensitively. No characters other than a-z allowed.
For Mastermind-style word games.
Arguments:
    - required: a word; use a hyphen ('-') in place of an unknown letter
    - optional: letters that occur somewhere in the word; a single hyphen ('-') = none
    - optional: letters that do not occur anywhere in the word
Examples:
    chu---       six-letter  words that start with 'chu'
    ---th ro     five-letter words that end   with 'th' and contain 'r' and 'o'
    ---th ro f   five-letter words that end   with 'th' and contain 'r' and 'o' but no 'f'
    v--- - e     four-letter words that start with 'v'  and don't contain 'e'\
"""

DICT_FILE = "/etc/dictionaries-common/words"  # one word per line

def parse_args():
    if not 2 <= len(sys.argv) <= 4:
        sys.exit(HELP_TEXT)

    arg1 = sys.argv[1].lower()
    if re.search(r"^[a-z-]+$", arg1) is None:
        sys.exit("Invalid first argument.")

    arg2 = sys.argv[2].lower() if len(sys.argv) >= 3 and sys.argv[2] != "-" else ""
    if re.search(r"^[a-z]*$", arg2) is None:
        sys.exit("Invalid second argument.")
    arg2 = set(arg2)
    if len(arg2) > arg1.count("-"):
        sys.exit("Can't have that many letters with unknown positions.")
    if arg2 & set(arg1):
        sys.exit("Second argument contains same letters as first argument.")

    arg3 = sys.argv[3].lower() if len(sys.argv) >= 4 else ""
    if re.search(r"^[a-z]*$", arg3) is None:
        sys.exit("Invalid third argument.")
    arg3 = set(arg3)
    if arg3 & (set(arg1) | arg2):
        sys.exit("Third argument contains letters specified in other arguments.")

    return (arg1, arg2, arg3)

def generate_words(length):
    # generate words of specified length
    regex = re.compile("^[A-Za-z]{" + str(length) + "}$")
    try:
        with open(DICT_FILE, "rt") as handle:
            handle.seek(0)
            yield from (w.rstrip("\n").lower() for w in handle if regex.search(w) is not None)
    except OSError:
        sys.exit("Error reading the dictionary file.")

def generate_user_specified_words(words, arg1, arg2, arg3):
    regex = re.compile("^" + "".join(c if c != "-" else "." for c in arg1) + "$")
    yield from (
        w for w in words
        if regex.search(w) is not None and arg2.issubset(set(w)) and arg3.isdisjoint(set(w))
    )

def main():
    (arg1, arg2, arg3) = parse_args()
    words = set(generate_words(len(arg1)))

    userSpecifiedWords = set(generate_user_specified_words(words, arg1, arg2, arg3))
    print("Words that match specified pattern:")
    if len(userSpecifiedWords) <= 10:
        for word in sorted(userSpecifiedWords):
            print("    " + word.upper())
    else:
        print("    (too many to show)")

    # count letters in words that match specified pattern (only once per word)
    letterCnts = collections.Counter()
    for word in userSpecifiedWords:
        letterCnts.update(set(word))
    unknownLetters = set(letterCnts) - set(arg1) - arg2 - arg3
    print("Unknown letters:", " ".join(sorted(l.upper() for l in unknownLetters)))

    # print words that contain many common unknown letters
    # (note: search all words of correct length, not only those that match user-specified pattern)
    words = sorted(words)
    words.sort(key=lambda w: sum(letterCnts[l] for l in set(w) & unknownLetters), reverse=True)
    print("Words with many common unknown letters:")
    for word in words[:10]:
        print("    {word} (score={score})".format(
            word=word.upper(),
            score=sum(letterCnts[l] for l in set(word) & unknownLetters)
        ))

main()
