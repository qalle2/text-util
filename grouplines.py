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

substrCounts = collections.Counter()
lines = (l.rstrip("\n") for l in sys.stdin)
if length > 0:
    substrCounts.update(l[:length] for l in lines)
else:
    substrCounts.update(l[length:] for l in lines)

for substr in substrCounts:
    print(f'"{substr}",{substrCounts[substr]}')
