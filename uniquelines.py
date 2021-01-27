"""Print unique lines from stdin."""

import sys

def main():
    lines = set(line[:-1] if line.endswith("\n") else line for line in sys.stdin)
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
