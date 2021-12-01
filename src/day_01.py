# Standard Library
from itertools import pairwise

# First Party
from utils import input_to_ints, ints_to_input, read_input


def part_1(input: str) -> int:
    depths = input_to_ints(input)

    return sum(b > a for a, b in pairwise(depths))


def part_2(input: str) -> int:
    depths = input_to_ints(input)
    depthWindows = ints_to_input(sum(depths[i : i + 3]) for i in range(len(depths) - 2))

    return part_1(depthWindows)


# -- Tests


def get_example_input() -> str:
    return """199
200
208
210
200
207
240
269
260
263"""


def test_part_1():
    assert part_1(get_example_input()) == 7


def test_part_2():
    assert part_2(get_example_input()) == 5


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 1688


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1728


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
