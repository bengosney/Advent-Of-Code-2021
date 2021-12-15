# Standard Library
import sys
from functools import lru_cache

# First Party
from utils import read_input

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


def part_1(input: str) -> int:
    grid = parse_input(input)
    target, _ = min_max(grid)
    visited = []
    path = []
    paths = []
    bob = [sum(grid.values()), 610]

    @lru_cache(maxsize=None)
    def walk(position: Position, score: int) -> None | int:
        current_score = score + grid[position]
        if current_score > min(bob):
            return

        if position == target:
            bob.append(current_score)
            paths.append(",".join(map(str, path)))
            return

        visited.append(position)
        path.append(grid[position])

        neighbors = []
        for neighbor in get_neighbors(position):
            if neighbor in grid and neighbor not in visited:
                neighbors.append(neighbor)

        sorted_n = sorted(neighbors, key=lambda n: grid[n])
        for neighbor in sorted_n:
            walk(neighbor, current_score)

        visited.remove(position)
        path.remove(grid[position])

        return

    walk((0, 0), -grid[(0, 0)])
    return min(bob)


def part_2(input: str) -> int:
    pass


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


# def test_part_2():
#     input = get_example_input()
#     assert part_2(input) is not None


# def test_part_1_real():
#     input = read_input(__file__)
#     assert part_1(input) is not None

# def test_part_1_real_fail1():
#    input = read_input(__file__)
#    assert part_1(input) < 610


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
