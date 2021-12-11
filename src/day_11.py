# Standard Library
import os
import textwrap
from math import sqrt

# First Party
from utils import read_input

# Type

Position = tuple[int, int]
Grid = dict[Position, int]


def get_grid(input: str) -> Grid:
    grid: Grid = {}
    for y, row in enumerate(input.splitlines()):
        for x, cell in enumerate(row):
            grid[(x, y)] = int(cell)

    return grid


def neighbors(position: Position) -> list[Position]:
    x, y = position
    return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]


def flash(grid: Grid, position: Position, flashed: set[Position]) -> tuple[Grid, set[Position]]:
    if position not in flashed:
        flashed.add(position)
        for neighbor in [n for n in neighbors(position) if n in grid]:
            grid[neighbor] += 1
            if grid[neighbor] >= 10:
                flash(grid, neighbor, flashed)

    return grid, flashed


def flattenForTesting(grid: Grid) -> str:
    flat = "".join(map(str, grid.values()))
    lines = textwrap.wrap(flat, int(sqrt(len(flat))))
    return "\n".join(lines)


def step(grid: Grid) -> tuple[Grid, int]:
    flashed: set[Position] = set()
    for position in grid:
        grid[position] += 1

    for position in grid:
        if grid[position] == 10:
            grid, newFlashed = flash(grid, position, flashed)
            flashed |= newFlashed

    for position in flashed:
        grid[position] = 0

    return grid, len(flashed)


def part_1(input: str) -> int:
    grid: Grid = get_grid(input)

    flashes = 0
    for _ in range(100):
        grid, stepFlashes = step(grid)
        flashes += stepFlashes

    return flashes


def part_2(input: str) -> int:
    grid: Grid = get_grid(input)

    flashes = 0
    octopuses = len(grid)
    steps = 0
    while flashes != octopuses:
        grid, flashes = step(grid)
        steps += 1

    return steps


# -- Tests


def get_example_input() -> str:
    return """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 1656


def test_step_function():
    grid = get_grid(
        """11111
19991
19191
19991
11111"""
    )

    grid, _ = step(grid)
    assert flattenForTesting(grid) == "34543\n40004\n50005\n40004\n34543"

    grid, _ = step(grid)
    assert flattenForTesting(grid) == "45654\n51115\n61116\n51115\n45654"


def test_steps():
    with open(os.path.join(os.path.dirname(__file__), "..", "inputs", "day_11_test.txt")) as f:
        test_data = f.read().strip().strip("\n\r")
    test_sections = [line.split("\n") for line in test_data.split("\n\n")]
    tests = {}
    for section in test_sections:
        stepNumber = int([i for i in section[0].replace(":", "").split() if i.isdigit()][0])
        tests[stepNumber] = section[1:]

    grid = get_grid(get_example_input())

    for stepNumber in range(1, max(tests.keys()) + 1):
        grid, _ = step(grid)
        if stepNumber in tests:
            assert flattenForTesting(grid) == "\n".join(tests[stepNumber])


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 195


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 1588


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 517


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
