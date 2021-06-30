import sys, unicodedata

# replacements made in addition to unicodedata.decomposition()
# Note: don't be language-specific! Interpret letters by what they look like, e.g. Æ = AE (not Ae),
# ß = sz (not ss), þ = none (not t/th).
#
ADDITIONAL_REPLACEMENTS = {
    # Latin-1 Supplement (U+0080...U+00FF); note: no thorn
    "Æ": "AE",
    "Ð": "D",
    "Ø": "O",
    "ß": "sz",
    "æ": "ae",
    "ð": "d",
    "ø": "o",
    # Latin Extended-A (U+0100...U+017F)
    "Đ": "D",
    "đ": "d",
    "Ħ": "H",
    "ħ": "h",
    "ı": "i",
    "Ĳ": "IJ",
    "ĳ": "ij",
    "ĸ": "k",
    "Ŀ": "L",
    "ŀ": "l",
    "Ł": "L",
    "ł": "l",
    "ŉ": "'n",
    "Ŋ": "N",
    "ŋ": "n",
    "Œ": "OE",
    "œ": "oe",
    "Ŧ": "T",
    "ŧ": "t",
    "ſ": "s",
    # Latin Extended-B (U+0180...U+024F) (incomplete)
    "Ǆ": "DZ",
    "ǅ": "Dz",
    "ǆ": "dz",
    "Ǉ": "LJ",
    "ǈ": "Lj",
    "ǉ": "lj",
    "Ǌ": "NJ",
    "ǋ": "Nj",
    "ǌ": "nj",
    "Ǳ": "DZ",
    "ǲ": "Dz",
    "ǳ": "dz",
    # Latin Extended Additional (U+1E00-U+1EFF) (incomplete)
    "ẞ": "SZ",
}

def decompose(char):
    # if character decomposes into an ASCII character, return it, otherwise "?"
    # first try the table of exceptions...
    try:
        return ADDITIONAL_REPLACEMENTS[char]
    except KeyError:
        pass
    # ...then unicodedata (recurse if decomposition is not ASCII)
    deco = unicodedata.decomposition(char).split(" ")[0]
    if len(deco) == 4 and set(deco).issubset(set("0123456789ABCDEF")):
        deco = int(deco, 16)
        if deco <= 0x7f:
            return chr(deco)
        return decompose(chr(deco))
    return "?"

def main():
    for line in sys.stdin:
        print("".join(
            (c if ord(c) <= 0x7f else decompose(c)) for c in line.rstrip("\n")
        ))

if __name__ == "__main__":
    main()
