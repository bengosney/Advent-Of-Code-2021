# Standard Library
from math import prod

# First Party
from utils import read_input

# Types

Position = tuple[int, int]
Grid = dict[Position, int]


def get_grid(input: str) -> Grid:
    lines = input.splitlines()
    grid: Grid = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)

    return grid


def get_adjacent(grid: Grid, position: Position) -> Grid:
    x, y = position
    adjacent_positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return {adjacent: grid[adjacent] for adjacent in adjacent_positions if adjacent in grid}


def get_adjacent_min(grid: Grid, position: Position) -> int:
    return min(get_adjacent(grid, position).values())


def get_lowpoints(grid: Grid) -> Grid:
    return {position: grid[position] + 1 for position, height in grid.items() if height < get_adjacent_min(grid, position)}


def part_1(input: str) -> int:
    grid = get_grid(input)

    return sum(get_lowpoints(grid).values())


def find_basin(grid: Grid, position: Position) -> set[Position]:
    out: set[Position] = {position}
    for adjacent_position, height in get_adjacent(grid, position).items():
        if height > grid[position] and height < 9:
            out |= find_basin(grid, adjacent_position)

    return out


def part_2(input: str) -> int:
    grid = get_grid(input)
    lowpoints = get_lowpoints(grid).keys()

    basins: list[int] = []
    for lowpoint in lowpoints:
        adj = find_basin(grid, lowpoint)
        basins.append(len(adj))

    return prod(sorted(basins)[-3:])


# -- Tests


def get_example_input() -> str:
    return """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 15


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 1134


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 475


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1092012


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
