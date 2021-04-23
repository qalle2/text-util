import collections, sys

if len(sys.argv) != 2:
    sys.exit(
        "Group lines from stdin by prefix (LENGTH > 0), suffix (LENGTH < 0) or entire line "
        "(LENGTH = 0). Print number of lines in each group. Argument: LENGTH"
    )

try:
    length = int(sys.argv[1], 10)
except ValueError:
    sys.exit("LENGTH must be an integer.")

# count prefixes/suffixes/entire lines from stdin
substrCounts = collections.Counter()
if length > 0:
    substrCounts.update(l.rstrip("\n")[:length] for l in sys.stdin)
else:
    substrCounts.update(l.rstrip("\n")[length:] for l in sys.stdin)

# sort normally, then case-insensitively, then by descending count
substrings = sorted(substrCounts)
substrings.sort(key=lambda s: s.casefold())
substrings.sort(key=lambda s: substrCounts[s], reverse=True)

for substring in substrings:
    print(f'"{substring}",{substrCounts[substring]}')
