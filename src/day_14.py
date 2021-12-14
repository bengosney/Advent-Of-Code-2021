# Standard Library
from collections import Counter, deque
from itertools import pairwise

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


def do_work(inital: str, pairs: Pairs, rounds: int) -> int:
    pair_counts = Counter(["".join(pair) for pair in pairwise(inital)])
    elements = Counter(inital)

    for _ in range(rounds):
        for pair, count in pair_counts.copy().items():
            pair_counts[pair] -= count
            elements[pairs[pair]] += count
            pair_counts[f"{pair[0]}{pairs[pair]}"] += count
            pair_counts[f"{pairs[pair]}{pair[1]}"] += count

    most_common = elements.most_common()
    return most_common[0][1] - most_common[-1][1]


def part_1(input: str) -> int:
    inital, pairs = parse_input(input)
    return do_work(inital, pairs, 10)


def part_2(input: str) -> int:
    inital, pairs = parse_input(input)
    return do_work(inital, pairs, 40)


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


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 2188189693529


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 3118


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 4332887448171


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
