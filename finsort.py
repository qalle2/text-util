"""Print lines from stdin in case-insensitive Finnish order.
See http://www.jkorpela.fi/kielenopas/4.15.html"""

import sys

# lower case letters (codepoints < 0x180) to replace for sorting
REPLACEMENTS = {
    # note: swap "ä" (and "æ") with "å" ("ä" and "å" have adjacent codepoints)
    ord("à"): "a",
    ord("á"): "a",
    ord("â"): "a",
    ord("ã"): "a",
    ord("ä"): "å",
    ord("å"): "ä",
    ord("æ"): "å",
    ord("ā"): "a",
    ord("ă"): "a",
    ord("ą"): "a",

    ord("ç"): "c",
    ord("ć"): "c",
    ord("ĉ"): "c",
    ord("ċ"): "c",
    ord("č"): "c",

    ord("ð"): "d",
    ord("ď"): "d",
    ord("đ"): "d",  # or "dj"?

    ord("è"): "e",
    ord("é"): "e",
    ord("ê"): "e",
    ord("ë"): "e",
    ord("ē"): "e",
    ord("ĕ"): "e",
    ord("ė"): "e",
    ord("ę"): "e",
    ord("ě"): "e",

    ord("ĝ"): "g",
    ord("ğ"): "g",
    ord("ġ"): "g",
    ord("ģ"): "g",

    ord("ĥ"): "h",
    ord("ħ"): "h",

    ord("ì"): "i",
    ord("í"): "i",
    ord("î"): "i",
    ord("ï"): "i",
    ord("ĩ"): "i",
    ord("ī"): "i",
    ord("ĭ"): "i",
    ord("į"): "i",
    ord("ı"): "i",

    ord("ĵ"): "j",

    ord("ķ"): "k",

    ord("ĺ"): "l",
    ord("ļ"): "l",
    ord("ľ"): "l",
    ord("ŀ"): "l",
    ord("ł"): "l",

    ord("ń"): "n",
    ord("ņ"): "n",
    ord("ň"): "n",
    ord("ŋ"): "ng",  # or "n"?

    # note: keep "ö"
    ord("ò"): "o",
    ord("ó"): "o",
    ord("ô"): "o",
    ord("õ"): "ö",
    ord("ø"): "ö",
    ord("ō"): "o",
    ord("ŏ"): "o",
    ord("ő"): "ö",
    ord("œ"): "oe",

    ord("ŕ"): "r",
    ord("ŗ"): "r",
    ord("ř"): "r",

    ord("ß"): "ss",
    ord("ś"): "s",
    ord("ŝ"): "s",
    ord("ş"): "s",
    ord("š"): "s",

    ord("þ"): "th",
    ord("ţ"): "t",
    ord("ť"): "t",
    ord("ŧ"): "t",

    ord("ù"): "u",
    ord("ú"): "u",
    ord("û"): "u",
    ord("ü"): "y",
    ord("ũ"): "u",
    ord("ū"): "u",
    ord("ŭ"): "u",
    ord("ů"): "u",
    ord("ű"): "y",
    ord("ų"): "u",

    # note: replace "w" with "v"
    ord("w"): "v",
    ord("ŵ"): "v",

    ord("ý"): "y",
    ord("ÿ"): "y",
    ord("ŷ"): "y",

    ord("ź"): "z",
    ord("ż"): "z",
    ord("ž"): "z",
}

lines = sorted(l.rstrip("\n") for l in sys.stdin)
for line in sorted(lines, key=lambda l: l.lower().translate(REPLACEMENTS)):
    print(line)
