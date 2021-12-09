# Standard Library
from math import prod

# First Party
from utils import read_input


def part_1(input: str) -> int:
    lines = input.splitlines()
    grid = {}
    width = 0
    height = 0
    maxheight = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
            maxheight = max(maxheight, int(c))
            width = max(width, x)
            height = max(height, y)

    lowpoints = []
    for y in range(height + 1):
        for x in range(width + 1):
            adj = min(
                [
                    grid.get((x - 1, y), maxheight),
                    grid.get((x + 1, y), maxheight),
                    grid.get((x, y - 1), maxheight),
                    grid.get((x, y + 1), maxheight),
                ]
            )
            if grid[(x, y)] < adj:
                lowpoints.append(grid[(x, y)] + 1)

    return sum(lowpoints)


def count_adjacent(grid: dict[tuple[int, int], int], x: int, y: int) -> set[tuple[int, int]]:
    adj = [
        (grid.get((x - 1, y), 0), (x - 1, y)),
        (grid.get((x + 1, y), 0), (x + 1, y)),
        (grid.get((x, y - 1), 0), (x, y - 1)),
        (grid.get((x, y + 1), 0), (x, y + 1)),
    ]

    out: set[tuple[int, int]] = {(x, y)}
    for a, (nx, ny) in adj:
        if a > grid[(x, y)] and a < 9:
            out |= count_adjacent(grid, nx, ny)

    return out


def part_2(input: str) -> int:
    lines = input.splitlines()
    grid = {}
    width = 0
    height = 0
    maxheight = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
            maxheight = max(maxheight, int(c))
            width = max(width, x)
            height = max(height, y)

    lowpoints = []
    for y in range(height + 1):
        for x in range(width + 1):
            adj = min(
                [
                    grid.get((x - 1, y), maxheight),
                    grid.get((x + 1, y), maxheight),
                    grid.get((x, y - 1), maxheight),
                    grid.get((x, y + 1), maxheight),
                ]
            )
            if grid[(x, y)] < adj:
                lowpoints.append((x, y))

    basins: list[int] = []
    for lowpoint in lowpoints:
        adj = count_adjacent(grid, *lowpoint)
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
