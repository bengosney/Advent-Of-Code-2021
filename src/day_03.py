# Standard Library
from collections import Counter

# First Party
from utils import read_input

# Third Party
from icecream import ic


def gamma(input: list[str]) -> int:
    result = ""
    # bits = defaultdict(lambda: Counter())
    for row in input:
        bits = [row[p] for p in range(len(row))]

        bit, _ = Counter(bits).most_common()[0]
        result += bit
    ic(result)
    return int(result, 2)


def epsilon(input: list[str]) -> int:
    pass


def part_1(input: str) -> int:
    pass


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_part_1():
    assert part_1(get_example_input()) == 198


def test_gamma():
    assert gamma(get_example_input().splitlines()) == 22


def test_epsilon():
    assert epsilon(get_example_input().splitlines()) == 9


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
