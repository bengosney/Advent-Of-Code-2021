# Standard Library
from collections import defaultdict
from typing import Iterator

# First Party
from utils import read_input

Position = tuple[int, int]
Fold = tuple[str, int]
Grid = dict[Position, str]


def parse_coords(input: list[str]) -> Iterator[Position]:
    for line in input:
        x, y = line.split(",")
        yield (int(x), int(y))


def parse_folds(input: list[str]) -> Iterator[Fold]:
    for line in input:
        _, _, part = line.split(" ")
        axis, value = part.split("=")
        yield (axis, int(value))


def min_max(grid: Grid) -> tuple[tuple[int, int], tuple[int, int]]:
    x_max = max(x for x, _ in grid)
    y_max = max(y for _, y in grid)
    x_min = min(x for x, _ in grid)
    y_min = min(y for _, y in grid)

    return (x_max, y_max), (x_min, y_min)


def draw(grid: Grid) -> None:
    (max_x, max_y), (min_x, min_y) = min_max(grid)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[(x, y)], end="")
        print()
    print()


def fold_grid(grid: Grid, fold: Fold) -> Grid:
    axis, value = fold
    (max_x, max_y), (min_x, min_y) = min_max(grid)

    if axis == "x":
        for x in range((max_x + 1) - value):
            for y in range(min_y, max_y + 1):
                if grid[(value + x, y)] == "#":
                    grid[(value - x, y)] = grid[(value + x, y)]
                del grid[(value + x, y)]

    elif axis == "y":
        for y in range((max_y + 1) - value):
            for x in range(min_x, max_x + 1):
                if grid[(value + y, x)] == "#":
                    grid[(value - y, x)] = grid[(value + y, x)]
                del grid[(value + y, x)]

    return grid


def part_1(input: str) -> int:
    raw_cords, raw_folds = input.split("\n\n")
    cords = parse_coords(raw_cords.split("\n"))
    folds = parse_folds(raw_folds.split("\n"))

    grid = defaultdict(lambda: ".")
    for position in cords:
        grid[position] = "#"

    for fold in folds:
        grid = fold_grid(grid, fold)
        break

    return sum(1 for _, v in grid.items() if v == "#")


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


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 735


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
