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


def get_adjcent(grid: Grid, position: Position, default: int) -> Grid:
    x, y = position
    return {
        (x - 1, y): grid.get((x - 1, y), default),
        (x + 1, y): grid.get((x + 1, y), default),
        (x, y - 1): grid.get((x, y - 1), default),
        (x, y + 1): grid.get((x, y + 1), default),
    }


def get_lowpoints(grid: Grid) -> Grid:
    maxheight = max(grid.values())
    lowpoints = {}
    for position, height in grid.items():
        adjcent = get_adjcent(grid, position, maxheight)
        if height < min(adjcent.values()):
            lowpoints[position] = grid[position] + 1

    return lowpoints


def part_1(input: str) -> int:
    grid = get_grid(input)

    lowpoints = get_lowpoints(grid)

    return sum(lowpoints.values())


def count_adjacent(grid: Grid, position: Position) -> set[tuple[int, int]]:
    x, y = position

    adjacent_cells = get_adjcent(grid, (x, y), 0)

    out: set[tuple[int, int]] = {(x, y)}
    for adjacent_position, adjacent in adjacent_cells.items():
        if adjacent > grid[(x, y)] and adjacent < 9:
            out |= count_adjacent(grid, adjacent_position)

    return out


def part_2(input: str) -> int:
    grid = get_grid(input)
    lowpoints = get_lowpoints(grid).keys()

    basins: list[int] = []
    for lowpoint in lowpoints:
        adj = count_adjacent(grid, lowpoint)
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
