# First Party
from utils import read_input


def part_1(input: str) -> int:
    crabs = list(map(int, input.split(",")))

    def move_crabs_to(crabs: list[int], position: int) -> int:
        return sum(abs(position - crab) for crab in crabs)

    min_fuel = 99999999999
    for position in range(len(crabs)):
        min_fuel = min(min_fuel, move_crabs_to(crabs, position))

    return min_fuel


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def part_2(input: str) -> int:
    crabs = list(map(int, input.split(",")))

    def move_crabs_to(crabs: list[int], position: int) -> int:
        pass

    min_fuel = 99999999999
    for position in range(len(crabs)):
        min_fuel = min(min_fuel, move_crabs_to(crabs, position))

    return min_fuel


# -- Tests


def get_example_input() -> str:
    return """16,1,2,0,4,2,7,1,2,14"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 37


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 168


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 349769


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
