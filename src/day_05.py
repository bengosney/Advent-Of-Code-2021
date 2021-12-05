# Standard Library
from collections import defaultdict
from math import atan2, degrees
from typing import Iterable

# First Party
from utils import read_input

Point = tuple[int, int]
Line = tuple[Point, Point]


def parse_input(input: str) -> Iterable[Line]:
    def parse_line(line: str) -> Line:
        def parse_coordinate(coordinate: str) -> Point:
            x, y = coordinate.split(",")
            return int(x), int(y)

        parts = line.split(" -> ")
        return parse_coordinate(parts[0]), parse_coordinate(parts[1])

    return [parse_line(line) for line in input.splitlines()]


def inc(x: int) -> int:
    return (x > 0) - (x < 0)


def valid(line: Line, valid_angles: int) -> bool:
    (x1, y1), (x2, y2) = line

    return abs(degrees(atan2(x1 - x2, y1 - y2))) in range(0, 360, valid_angles)


def count_overlaps(lines: Iterable[Line], valid_angles: int) -> int:
    valid_lines = [line for line in lines if valid(line, valid_angles)]
    grid: dict[Point, int] = defaultdict(lambda: 0)

    for (x1, y1), (x2, y2) in valid_lines:
        incX, incY = inc(x2 - x1), inc(y2 - y1)
        while (x1, y1) != (x2 + incX, y2 + incY):
            grid[(x1, y1)] += 1
            x1 += incX
            y1 += incY

    return len([g for g in grid.values() if g > 1])


def part_1(input: str) -> int:
    lines = parse_input(input)
    return count_overlaps(lines, 90)


def part_2(input: str) -> int:
    lines = parse_input(input)
    return count_overlaps(lines, 45)


# -- Tests


def get_example_input() -> str:
    return """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_part_1():
    assert part_1(get_example_input()) == 5


def test_part_2():
    assert part_2(get_example_input()) == 12


def test_part_2_fail1():
    assert part_2(read_input(__file__)) > 19236


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 6841


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 19258


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
