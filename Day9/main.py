#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = True


def part1(input):
    pass


def part2(input):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = data.read_lines()

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
