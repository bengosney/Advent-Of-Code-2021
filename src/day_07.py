# Standard Library
import multiprocessing as mp
import sys
from functools import lru_cache, partial

# First Party
from utils import read_input


def move_crabs_to(crabs: list[int], position: int) -> int:
    return sum(abs(position - crab) for crab in crabs)


def part_1(input: str) -> int:
    crabs = list(map(int, input.split(",")))

    min_fuel = sys.maxsize
    for position in range(len(crabs)):
        min_fuel = min(min_fuel, move_crabs_to(crabs, position))

    return min_fuel


def move_crabs_to_exp(position: int, crabs: list[int]) -> int:
    return sum(move_crab_exp(abs(position - crab)) for crab in crabs)


@lru_cache(maxsize=None)
def move_crab_exp(distance: int) -> int:
    return ((distance * distance) + distance) // 2


def part_2(input: str) -> int:
    crabs: list[int] = list(map(int, input.split(",")))

    process_crabs = partial(move_crabs_to_exp, crabs=crabs)
    pool = mp.Pool(mp.cpu_count())
    fuel = pool.map(process_crabs, range(len(crabs)))

    return min(fuel)


# -- Tests


def get_example_input() -> str:
    return """16,1,2,0,4,2,7,1,2,14"""


def test_move_exp():
    moves = [
        (11, 66),
        (4, 10),
        (3, 6),
        (5, 15),
        (1, 1),
        (3, 6),
        (2, 3),
        (4, 10),
        (3, 6),
        (9, 45),
    ]
    for distance, fuel in moves:
        assert move_crab_exp(distance) == fuel


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 37


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 168


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 349769


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 99540554


# -- Main


if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
