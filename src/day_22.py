# Standard Library
import re
from dataclasses import dataclass
from itertools import pairwise, product

# First Party
from utils import read_input

RangePair = tuple[int, int]


@dataclass
class Range:
    x: RangePair
    y: RangePair
    z: RangePair

    def subtract(self: "Range", other: "Range") -> list["Range"]:
        return Range(
            x=self.x[0] - other.x[0],
            y=self.y[0] - other.y[0],
            z=self.z[0] - other.z[0],
        )


def parse_lint(input: str) -> tuple[bool, RangePair, RangePair, RangePair]:
    regex = r"^(on|off)[\s,][xyz]=(-?\d+)..(-?\d+)[\s,][xyz]=(-?\d+)..(-?\d+)[\s,][xyz]=(-?\d+)..(-?\d+)"

    matches = re.finditer(regex, input, re.MULTILINE)
    for match in matches:
        groups = match.groups()
        onoff = True if groups[0] == "on" else False
        vals = list(map(int, groups[1:]))
        ranges = list(pairwise(vals))

        return onoff, ranges[0], ranges[1], ranges[2]

    raise Exception(f"No match found: {input}")


def part_1(input: str) -> int:
    grid = set()

    for line in input.splitlines():
        onoff, xrange, yrange, zrange = parse_lint(line)
        current = set()
        for key in product(xrange, yrange, zrange):
            current.add(key)

        if onoff:
            grid |= current
        else:
            grid -= current

        print(len(grid))

    return len(grid)


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 39


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
