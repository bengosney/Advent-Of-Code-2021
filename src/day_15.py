# Standard Library
import sys

# First Party
from utils import read_input

# Third Party
import networkx as nx

Position = tuple[int, int]
Grid = dict[Position, int]

sys.setrecursionlimit(15000)


def parse_input(input: str) -> Grid:
    grid: Grid = {}
    for y, row in enumerate(input.split("\n")):
        for x, val in enumerate(row):
            grid[(x, y)] = int(val)

    return grid


def get_neighbors(position: Position) -> list[Position]:
    x, y = position
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def min_max(grid: Grid) -> tuple[Position, Position]:
    x, y = zip(*grid)

    return (max(x), max(y)), (min(x), min(y))


def solve(grid: Grid) -> int:
    (tx, ty), _ = min_max(grid)
    cave = nx.grid_2d_graph(tx, ty, create_using=nx.DiGraph)
    for y in range(ty + 1):
        for x in range(tx + 1):
            for n in get_neighbors((x, y)):
                if n in grid:
                    cave.add_edge(n, (x, y), weight=grid[n])

    return nx.dijkstra_path_length(cave, (0, 0), (tx, ty))


def part_1(input: str) -> int:
    grid = parse_input(input)
    return solve(grid)


def part_2(input: str) -> int:
    grid = parse_input(input)
    (w_, h_), _ = min_max(grid)
    w = w_ + 1
    h = h_ + 1
    expanded_grid: Grid = grid.copy()

    new_w = w * 5
    new_h = h * 5
    for x in range(w, new_w):
        for y in range(h):
            expanded_grid[(x, y)] = expanded_grid.get((x, y), expanded_grid[(x - w, y)] % 9 + 1)

    for x in range(new_w):
        for y in range(h, new_h):
            expanded_grid[(x, y)] = expanded_grid.get((x, y), expanded_grid[(x, y - w)] % 9 + 1)

    return solve(expanded_grid)


# -- Tests


def get_example_input() -> str:
    return """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 40


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 315


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) is not None


def test_part_1_real_fail1():
    input = read_input(__file__)
    assert part_1(input) < 610


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
