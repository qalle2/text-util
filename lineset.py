"""Read one or more text files. Output the setwise union, intersection or difference of the lines
without duplicates."""

import sys

def read_lines(name):
    """Return lines as a set."""

    try:
        with open(name, "rt", encoding="utf8") as handle:
            handle.seek(0)
            return set((line[:-1] if line.endswith("\n") else line) for line in handle)
    except UnicodeDecodeError:
        sys.exit("Not a UTF-8 text file.")
    except OSError:
        sys.exit("Error reading file.")

def get_results():
    """Return lines as a set."""

    (operation, files) = (sys.argv[1], sys.argv[2:])

    # read lines from first file
    lines = set(read_lines(files[0]))

    # update results with other input files
    if operation == "u":
        function = lines.update
    elif operation == "i":
        function = lines.intersection_update
    elif operation == "d":
        function = lines.difference_update
    else:
        sys.exit("Operations allowed: u=union, i=intersection, d=difference")
    for file_ in files[1:]:
        function(read_lines(file_))

    return lines

def main():
    if len(sys.argv) < 3:
        sys.exit("Args: OPERATION FILE1 [FILE2 ...]")
    for line in get_results():
        print(line)

if __name__ == "__main__":
    main()
