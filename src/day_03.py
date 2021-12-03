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


def mostCommon(input: list[str], position: int) -> str:
    bits = ["1"]
    for row in input:
        bits.append(row[position])

    bits.append("0")

    return Counter(bits).most_common()[0][0]


def leastCommon(input: list[str], position: int) -> str:
    bits = ["1"]
    for row in input:
        bits.append(row[position])

    bits.append("0")

    return Counter(bits).most_common()[-1][0]


def o2(input: list[str], p=0) -> int:
    left: list[str] = []

    c = mostCommon(input, p)
    left = [row for row in input if row[p] == c]

    if len(left) == 1:
        return int(left[0], 2)
    else:
        return o2(left, p + 1)


def co2(input: list[str], p=0) -> int:
    left: list[str] = []

    c = leastCommon(input, p)
    left = [row for row in input if row[p] == c]

    if len(left) == 1:
        return int(left[0], 2)
    else:
        return co2(left, p + 1)


def part_1(input: str) -> int:
    lines = input.splitlines()
    return gamma(lines) * epsilon(lines)


def part_2(input: str) -> int:
    lines = input.splitlines()
    return o2(lines) * co2(lines)


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


def test_o2():
    assert o2(get_example_input().splitlines()) == 23


def test_co2():
    assert co2(get_example_input().splitlines()) == 10


def test_part_2():
    assert part_2(get_example_input()) == 230


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 3009600


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 6940518


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
