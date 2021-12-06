# Standard Library
from collections import defaultdict

# First Party
from utils import read_input


def process_fish(fish: dict[int, int], day: int) -> dict[int, int]:
    newFish = defaultdict(lambda: 0)

    for i in range(9):
        newFish[i - 1] = fish[i]

    newFish[8] = fish[0]
    newFish[6] += fish[0]
    del newFish[-1]

    return newFish


def part_1(input: str) -> int:
    fishInput = map(int, input.split(","))
    fish = defaultdict(lambda: 0)

    for f in fishInput:
        fish[f] += 1

    for d in range(80):
        fish = process_fish(fish, d + 1)

    return sum(list(fish.values()))


def part_2(input: str) -> int:
    fishInput = map(int, input.split(","))
    fish = defaultdict(lambda: 0)

    for f in fishInput:
        fish[f] += 1

    for d in range(256):
        fish = process_fish(fish, d + 1)

    return sum(list(fish.values()))


# -- Tests


def get_example_input() -> str:
    return """3,4,3,1,2"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 5934


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 26984457539


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 351188


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1595779846729


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
