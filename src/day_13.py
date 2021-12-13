# Standard Library
from collections import defaultdict
from typing import Iterator

# First Party
from utils import read_input

# Third Party
from icecream import ic

Position = tuple[int, int]
Fold = tuple[str, int]
Grid = dict[Position, str]


def parse_coords(input: list[str]) -> Iterator[Position]:
    for line in input:
        x, y = line.split(",")
        yield (int(x), int(y))


def parse_folds(input: list[str]) -> Iterator[Fold]:
    for line in input:
        _, _, part = line.split(",")
        axis, value = part.split("=")
        yield (axis, int(value))


def max_values(grid: Grid) -> tuple[int, int]:
    x_max = max(x for x, _ in grid)
    y_max = max(y for _, y in grid)

    return (x_max, y_max)


def fold(grid: Grid, fold: Fold) -> Grid:
    axis, value = fold
    max_x, max_y = max_values(grid)

    if axis == "x":
        for y in range(max_x):
            for x in range(value):
                grid[(x, y)] = "."


def part_1(input: str) -> int:
    raw_cords, raw_folds = input.split("\n\n")
    cords = parse_coords(raw_cords.split("\n"))
    # folds = parse_folds(raw_folds.split("\n"))

    grid = defaultdict(lambda: ".")
    for position in cords:
        grid[position] = "#"

    ic(cords)


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 17


# def test_part_2():
#     input = get_example_input()
#     assert part_2(input) is not None


# def test_part_1_real():
#     input = read_input(__file__)
#     assert part_1(input) is not None


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
