import collections, re, sys

DICT_FILE = "/etc/dictionaries-common/words"

# parse arguments
if not 2 <= len(sys.argv) <= 3:
    sys.exit(
        "Suggest words to begin a Mastermind-style game with. Arguments: "
        "word length, optionally a list of letters (a-z) to ignore."
    )
wordLen = int(sys.argv[1], 10)
ignoreLetters = set(sys.argv[2].lower()) if len(sys.argv) >= 3 else set()

# get words of correct length
with open(DICT_FILE, "rt") as handle:
    words = {
        w.rstrip("\n").lower() for w in handle
        if re.search("^[A-Za-z]{" + str(wordLen) + "}$", w) is not None
    }

# count letters (no more than once per word)
letterCnts = collections.Counter()
for word in words:
    letterCnts.update(set(word))
letterCnts = dict((l, letterCnts[l]) for l in set(letterCnts) - ignoreLetters)

# sort by score
words = sorted(words)
words.sort(
    key=lambda w: sum(letterCnts.get(l, 0) for l in set(w)), reverse=True
)
print("Words (no more than 10):")
for word in words[:10]:
    print("{word} (score={score})".format(
        word=word.upper(),
        score=sum(letterCnts.get(l, 0) for l in set(word))
    ))
