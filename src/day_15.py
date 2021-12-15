# First Party
from utils import read_input

# Third Party
from icecream import ic

Position = tuple[int, int]
Grid = dict[Position, int]


def parse_input(input: str) -> Grid:
    grid: Grid = {}
    for y, row in enumerate(input.split("\n")):
        for x, val in enumerate(row):
            grid[(x, y)] = int(val)

    return grid


def neighbors(position: Position) -> list[Position]:
    x, y = position
    return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]


def min_max(grid: Grid) -> tuple[Position, Position]:
    x, y = zip(*grid)

    return (max(x), max(y)), (min(x), min(y))


def walk(grid: Grid, position: Position, target: Position, visited: list[Position] = []) -> int:
    visited.append(position)
    scores = [0]

    if position == target:
        return grid[position]

    for neighbor in neighbors(position):
        if neighbor in grid and neighbor not in visited:
            scores.append(walk(grid, neighbor, target, visited.copy()))
    return min(scores) + grid[position]


def part_1(input: str) -> int:
    grid = parse_input(input)
    (x, y), _ = min_max(grid)
    ic(grid)
    ic(min_max(grid))

    return walk(grid, (0, 0), (x, y))


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


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
