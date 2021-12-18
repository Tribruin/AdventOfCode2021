#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = True
hex2bin = dict()
for i in range(16):
    hex2bin[f"{i:x}".upper()] = f"{i:04b}"


def parse_input(data_input):
    result = ""
    for i in data_input[0]:
        result += f"{hex2bin[i]}"
    return result


def parse_literal(code) -> list:

    numbers = list()

    leading_digit, partial_code = code[0], code[1:5]
    finished = False

    while not finished:
        numbers.append(int(partial_code, 2))
        if leading_digit == "0":
            finished = True
        else:
            code = code[5:]
            leading_digit, partial_code = code[0], code[1:5]

    return numbers


def split_code(code):

    V, T = int(code[0:3], 2), int(code[3:6], 2)
    code = code[6:]

    if T == 4:
        numbers = parse_literal(code)

    return V, T, numbers


def part1(code):
    values = list()
    V, T, result = split_code(code)
    print(V, T)
    joined_code = "".join([f"{x:04b}" for x in result])
    print(joined_code)
    print(f"{int(joined_code,2)}")


def part2(code):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
