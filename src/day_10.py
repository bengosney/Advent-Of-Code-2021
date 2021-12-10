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


def score_autocomplete(open):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = 0
    for c in open:
        score *= 5
        score += points[c]

    return score


def part_2(input: str) -> int:
    lines = input.splitlines()

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    scores = []
    for line in lines:
        errors, new_open = match_pair(line)
        if len(errors) != 0:
            continue
        closing = reversed([pairs[char] for char in new_open])
        scores.append(score_autocomplete(closing))

    scores = sorted(scores)
    return scores[len(scores) // 2]


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
    assert part_2(input) == 288957


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 436497


def test_score():
    pairs = {
        "])}>": 294,
        "}}]])})]": 288957,
        ")}>]})": 5566,
        "}}>}>))))": 1480781,
        "]]}}]}]}>": 995444,
    }
    for q, a in pairs.items():
        assert score_autocomplete(q) == a


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 2377613374


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
