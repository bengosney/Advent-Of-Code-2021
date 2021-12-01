# First Party
from utils import read_input


def part_1(input: str) -> int:
    pass


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """
    """


def test_part_1():
    assert part_1(get_example_input()) is not None


def test_part_2():
    assert part_2(get_example_input()) is not None


# def test_part_1_real():
#     input = read_input(__file__)
#     assert part_1(input) == None
#
# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) == None

# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
