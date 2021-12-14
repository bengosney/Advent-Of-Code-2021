# Standard Library
from collections import Counter, deque

# First Party
from utils import read_input

Pairs = dict[str, str]
Polymer = deque[str]


def parse_input(input: str) -> tuple[str, Pairs]:
    start, raw_pairs = input.split("\n\n")

    pairs = {}
    for raw_pair in raw_pairs.split("\n"):
        pair, new = raw_pair.split(" -> ")
        pairs[pair] = new

    return start, pairs


def do_round(working: Polymer, pairs: Pairs) -> Polymer:
    for _ in range(len(working) - 1):
        pair = working[0] + working[1]
        working.insert(1, pairs[pair])
        working.rotate(-2)

    working.rotate(-1)

    return working


def part_1(input: str) -> int:
    start, pairs = parse_input(input)
    working = deque([s for s in start])

    for _ in range(10):
        working = do_round(working, pairs)

    counts = Counter(working)

    _, most = counts.most_common()[0]
    _, least = counts.most_common()[-1]

    return most - least


def part_2(input: str) -> int:
    start, pairs = parse_input(input)
    working = deque([s for s in start])

    for i in range(40):
        print(i)
        working = do_round(working, pairs)

    counts = Counter(working)

    _, most = counts.most_common()[0]
    _, least = counts.most_common()[-1]

    return most - least


# -- Tests


def get_example_input() -> str:
    return """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 1588


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
