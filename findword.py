import re, os, sys

HELP_TEXT = """\
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

    arg3 = sys.argv[3].lower() if len(sys.argv) >= 4 else ""
    if re.search(r"^[a-z]*$", arg3) is None:
        sys.exit("Invalid third argument.")
    arg3 = set(arg3)

    return (arg1, arg2, arg3)

def get_words(regex):
    if not os.path.isfile(DICT_FILE):
        sys.exit("Dictionary file not found.")

    try:
        with open(DICT_FILE, "rt") as handle:
            yield from(
                w.rstrip("\n").lower() for w in handle
                if re.search(regex, w, re.IGNORECASE) is not None
            )
    except OSError:
        sys.exit("Error reading the dictionary file.")

def main():
    (arg1, arg2, arg3) = parse_args()
    regex = "^" + "".join(c if c != "-" else "[a-z]" for c in arg1) + "$"
    words = {w for w in get_words(regex) if arg2.issubset(set(w)) and arg3.isdisjoint(set(w))}
    for word in sorted(words):
        print(word)

main()
