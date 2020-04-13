"""Copy stdin to stdout and apply one of the Unicode Normalization Forms."""

import argparse
import sys
import unicodedata

def parse_arguments():
    """Parse command line arguments using argparse."""

    parser = argparse.ArgumentParser(
        description="Copy stdin to stdout and apply one of the Unicode Normalization Forms.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n", "--normalization", choices=("nfd", "nfc", "nfkd", "nfkc"), default="nfc",
        help="Which Unicode Normalization Form to apply to each line. See "
        "https://unicode.org/reports/tr15/#Norm_Forms"
    )

    return parser.parse_args()

def main():
    """The main function."""

    args = parse_arguments()
    for line in sys.stdin:
        line = line[:-1] if line.endswith("\n") else line
        line = unicodedata.normalize(args.normalization.upper(), line)
        print(line)

if __name__ == "__main__":
    main()
