# Standard Library
import re

# First Party
from utils import read_input

Position = tuple[int, int]
Target = tuple[Position, Position]


def parse_input(input: str) -> Target:
    regex = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"

    matches = re.finditer(regex, input, re.MULTILINE)
    for match in matches:
        x1, x2, y1, y2 = match.groups()

        return (min(int(x1), int(x2)), max(int(y1), int(y2))), (max(int(x1), int(x2)), min(int(y1), int(y2)))

    raise Exception("No match")


def part_1(input: str) -> int:
    target = parse_input(input)
    _, (_, max_y) = target

    y = abs(max_y)

    return int(y * ((y - 1) / 2))


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return "target area: x=20..30, y=-10..-5"


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 45


# def test_part_2():
#     input = get_example_input()
#     assert part_2(input) is not None


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 9870


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
