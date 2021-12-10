#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
import numpy as np
from scipy.ndimage import label

testing = False


def parse_input(data: AOC):

    lines = data.read_lines()
    num_array = np.genfromtxt(lines, dtype=int, delimiter=1)
    num_array = np.pad(num_array, 1, mode="constant", constant_values=9)

    return num_array


def get_neighbors(array: np.array, y: int, x: int) -> list():

    adjecent = [
        array[y - 1][x],
        array[y + 1][x],
        array[y][x - 1],
        array[y][x + 1],
    ]

    return adjecent


def part1(floor_array: np.array):
    y_size, x_size = np.shape(floor_array)
    low_points = np.full((y_size, x_size), False, dtype=bool)

    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            adjecent = get_neighbors(floor_array, y, x)

            # check if lowest
            # Mark the map True or False
            low_points[y][x] = (
                floor_array[y][x] < adjecent[0]
                and floor_array[y][x] < adjecent[1]
                and floor_array[y][x] < adjecent[2]
                and floor_array[y][x] < adjecent[3]
            )

    low_point_heights = floor_array * low_points
    print(np.sum(low_points) + np.sum(low_point_heights))


def part2(floor_array: np.array):

    # Used code from https://gitlab.com/AsbjornOlling/aoc2021/-/blob/master/09/solve.py
    # Did not know about label or bincount

    basins, _ = label(floor_array != 9)
    basin_areas = np.bincount(basins[basins != 0])
    top_three = np.sort(basin_areas)[-3:]
    print(top_three[0] * top_three[1] * top_three[2])


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    floor_array = parse_input(data)

    part1(floor_array)
    part2(floor_array)


if __name__ == "__main__":
    main()
