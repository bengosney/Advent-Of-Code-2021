# Standard Library

# Standard Library
from typing import Iterable

# First Party
from utils import read_input

# Types
SignalPattern = set[str]
SignalPatterns = Iterable[SignalPattern]


def parse_line(line: str) -> tuple[SignalPatterns, SignalPatterns]:
    def parse(string: str) -> SignalPatterns:
        return map(lambda s: set(s), string.strip().split(" "))

    patterns, output = line.split("|")

    return parse(patterns), parse(output)


def part_1(input: str) -> int:
    lines = [parse_line(line) for line in input.split("\n")]
    count = 0
    for line in lines:
        _, output = line
        count += len([o for o in output if len(o) in [2, 4, 3, 7]])

    return count


def decode(input: tuple[SignalPatterns, SignalPatterns]) -> int:
    patterns, outputs = input
    numbers: dict[int, SignalPattern] = {}
    unmatched: dict[int, list[SignalPattern]] = {5: [], 6: []}

    for pattern in patterns:
        length = len(pattern)
        if length == 2:
            numbers[1] = pattern
        elif length == 3:
            numbers[7] = pattern
        elif length == 4:
            numbers[4] = pattern
        elif length == 7:
            numbers[8] = pattern
        else:
            unmatched[length].append(pattern)

    segments = {}

    segments["a"] = numbers[7] - numbers[1]
    numbers[9] = [letters for letters in unmatched[6] if len(letters - (numbers[7] | numbers[4])) == 1][0]

    segments["g"] = numbers[9] - (numbers[7] | numbers[4])
    numbers[3] = [letters for letters in unmatched[5] if len(letters - (numbers[7] | segments["g"])) == 1][0]

    segments["b"] = numbers[9] - numbers[3]
    segments["e"] = numbers[8] - numbers[9]

    numbers[0] = numbers[7] | segments["g"] | segments["e"] | segments["b"]
    segments["d"] = numbers[8] - numbers[0]

    numbers[6] = [letters for letters in unmatched[6] if letters not in numbers.values()][0]

    segments["c"] = numbers[8] - numbers[6]
    segments["f"] = numbers[1] - segments["c"]

    numbers[2] = (numbers[3] | segments["e"]) - segments["f"]
    numbers[5] = numbers[6] - segments["e"]

    decodedDigits: list[str] = []
    for output in outputs:
        k = [str(k) for k, v in numbers.items() if output == v][0]
        decodedDigits.append(k)

    return int("".join(decodedDigits))


def part_2(input: str) -> int:
    lines = [parse_line(line) for line in input.split("\n")]
    tot = 0
    for line in lines:
        tot += decode(line)

    return tot


# -- Tests


def get_example_input() -> str:
    return """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 26


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 61229


def test_decode():
    assert decode(parse_line("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")) == 5353


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 479


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1041746


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
