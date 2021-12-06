# Standard Library
from collections import defaultdict

# First Party
from utils import read_input

# Third Party
from icecream import ic


def process_fish(fish: dict[int, int]) -> dict[int, int]:
    newFish = defaultdict(lambda: 0)

    for i in range(8):
        newFish[i - 1] = fish[i]

    newFish[8] = fish[-1]
    newFish[6] = fish[-1]
    del newFish[-1]

    return newFish


def part_1(input: str) -> int:
    fishInput = map(int, input.split(","))
    fish = defaultdict(lambda: 0)

    for f in fishInput:
        fish[f] += 1

    for _ in range(18):
        # ic(list(fish.values()))
        for i in range(8):
            ic(i, i - 1)
            fish[i - 1] = fish[i]

        fish[8] = fish[-1]
        fish[6] = fish[-1]
        del fish[-1]
        break

    return len(fish)


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """3,4,3,1,2"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 5934


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
