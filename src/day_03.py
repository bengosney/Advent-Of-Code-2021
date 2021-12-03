# Standard Library
from collections import Counter

# First Party
from utils import read_input


def gamma_epsilon(input: list[list[str]]) -> tuple[int, int]:
    bits = zip(*input[::-1])

    gamma = ""
    epsilon = ""
    for b in bits:
        gamma += Counter(b).most_common()[0][0]
        epsilon += Counter(b).most_common()[-1][0]

    return int(gamma, 2), int(epsilon, 2)


def part_1(input: str) -> int:
    gamma, epsilon = gamma_epsilon([list(line) for line in input.splitlines()])
    return gamma * epsilon


def commonality(input: list[str], position: int) -> tuple[str, str]:
    bits = ["1", "0"] + [row[position] for row in input]
    most_common = Counter(bits).most_common()

    return most_common[0][0], most_common[-1][0]


def o2_co2(input: list[str], type: int, position: int = 0) -> int:
    left: list[str] = []

    c = commonality(input, position)[type]
    left = [row for row in input if row[position] == c]

    if len(left) == 1:
        return int(left[0], 2)
    else:
        return o2_co2(left, type, position + 1)


def o2(input: list[str]) -> int:
    return o2_co2(input, 0)


def co2(input: list[str]) -> int:
    return o2_co2(input, 1)


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
    gamma, _ = gamma_epsilon([list(line) for line in get_example_input().splitlines()])
    assert gamma == 22


def test_epsilon():
    _, epsilon = gamma_epsilon([list(line) for line in get_example_input().splitlines()])
    assert epsilon == 9


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
