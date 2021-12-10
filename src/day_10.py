# Standard Library
from collections import Counter

# First Party
from utils import read_input


def match_pair(line):
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    open = []
    errors = []
    for char in line:
        if char in pairs:
            open.append(char)
        elif char != pairs[open.pop()]:
            errors.append(char)

    return errors, open


def part_1(input: str) -> int:
    lines = input.splitlines()

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    err = []
    for line in lines:
        new_errors, _ = match_pair(line)
        err += new_errors

    count = Counter(err)
    return sum(points[char] * count[char] for char in count)


def part_2(input: str) -> int:
    lines = input.splitlines()

    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    open = []
    for line in lines:
        _, new_open = match_pair(line)
        open += [pairs[char] for char in new_open]

    count = Counter(open)
    return sum(points[char] * count[char] for char in count)


# -- Tests


def get_example_input() -> str:
    return """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 26397


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 436497


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
