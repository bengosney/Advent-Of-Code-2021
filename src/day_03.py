# Standard Library
from collections import Counter, defaultdict

# First Party
from utils import read_input


def gamma(input: list[str]) -> int:
    bits = defaultdict(lambda: [])
    for row in input:
        for p in range(len(row)):
            bits[p].append(row[p])

    result = ""
    for p in bits:
        bit, _ = Counter(bits[p]).most_common()[0]
        result += bit

    return int(result, 2)


def epsilon(input: list[str]) -> int:
    bits = defaultdict(lambda: [])
    for row in input:
        for p in range(len(row)):
            bits[p].append(row[p])

    result = ""
    for p in bits:
        bit, _ = Counter(bits[p]).most_common()[-1]
        result += bit

    return int(result, 2)


def part_1(input: str) -> int:
    lines = input.splitlines()
    return gamma(lines) * epsilon(lines)


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


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 3009600


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) == None

# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
