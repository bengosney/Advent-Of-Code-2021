# Standard Library
from collections import defaultdict

# First Party
from utils import read_input

# Third Party
from icecream import ic


def sort_string(string: str) -> str:
    return "".join(sorted(string))


def sort_strings(strings: list[str]) -> list[str]:
    return list(map(sort_string, strings))


def split_string(string: str) -> list[str]:
    return [char for char in string]


def parse_line(line: str) -> tuple[list[str], list[str]]:
    patterns, output = line.split("|")
    return patterns.strip().split(" "), output.strip().split(" ")


def part_1(input: str) -> int:
    lines = [parse_line(line) for line in input.split("\n")]
    count = 0
    for line in lines:
        _, output = line
        count += len([o for o in output if len(o) in [2, 4, 3, 7]])

    return count


def decode(input: tuple[list[str], list[str]]) -> int:
    pattern, outputs = input
    mapping = defaultdict(lambda: set())
    others = {5: [], 6: []}

    for p in pattern:
        length = len(p)
        if length == 2:  # 1
            mapping[1] = {_ for _ in p}
        elif length == 3:  # 7
            mapping[7] = {_ for _ in p}
        elif length == 4:  # 4
            mapping[4] = {_ for _ in p}
        elif length == 7:  # 8
            mapping[8] = {_ for _ in p}
        else:
            others[length].append({_ for _ in p})

    maps = {}
    maps["a"] = mapping[7] - mapping[1]

    ic(mapping, maps)

    # return int("".join(output))


def part_2(input: str) -> int:
    # lines = [parse_line(line) for line in input.split("\n")]
    pass


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


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
