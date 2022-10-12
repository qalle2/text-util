import sys

def read_lines(filename):
    # generate lines from file
    try:
        with open(filename, "rt", encoding="utf8") as handle:
            handle.seek(0)
            yield from (l.rstrip("\n") for l in handle)
    except UnicodeDecodeError:
        sys.exit("Not a UTF-8 text file.")
    except OSError:
        sys.exit("Error reading file.")

def main():
    if len(sys.argv) < 3:
        sys.exit(
            "Print setwise union (OPERATION=u), intersection (OPERATION=i) "
            "or difference (OPERATION=d) of lines without duplicates. Args: "
            "OPERATION FILE1 [FILE2 ...]"
        )

    (operation, files) = (sys.argv[1], sys.argv[2:])

    try:
        method = {
            "u": set.update,
            "i": set.intersection_update,
            "d": set.difference_update
        }[operation]
    except KeyError:
        sys.exit("Invalid operation argument.")

    lines = set(read_lines(files[0]))

    for filename in files[1:]:
        method(lines, read_lines(filename))

    for line in lines:
        print(line)

main()
