# First Party
from utils import read_input

# Third Party
from icecream import ic


def part_1(input: str) -> int:
    bin = int(input, 16)
    ic(bin)


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """110100101111111000101000"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) is not None


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
