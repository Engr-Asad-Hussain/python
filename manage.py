import argparse
import subprocess


def black_formatter():
    commands = [["black", "."]]
    for cmd in commands:
        subprocess.run(cmd)


def isort_sorter():
    commands = [["isort", ".", "--profile", "black"]]
    for cmd in commands:
        subprocess.run(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--build",
        default=False,
        action="store_true",
        help="Format codebase using black and isort.",
    )
    parser.add_argument(
        "--black",
        default=False,
        action="store_true",
        help="Format codebase using black.",
    )
    parser.add_argument(
        "--isort",
        default=False,
        action="store_true",
        help="Format codebase using isort.",
    )
    args = parser.parse_args()
    if args.build is True:
        black_formatter()
        isort_sorter()
    elif args.black is True:
        black_formatter()
    elif args.isort is True:
        isort_sorter()
    else:
        ValueError("Unsupported argument.")
