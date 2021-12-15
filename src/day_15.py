# Standard Library
# Standard Library
from collections import defaultdict
from heapq import heappop, heappush

# First Party
from utils import read_input

Position = tuple[int, int]
Grid = dict[Position, int]
Graph = dict[Position, list[tuple[Position, int]]]


def parse_input(input: str) -> Grid:
    grid: Grid = {}
    for y, row in enumerate(input.split("\n")):
        for x, val in enumerate(row):
            grid[(x, y)] = int(val)

    return grid


def get_neighbors(position: Position) -> list[Position]:
    x, y = position
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def grid_max(grid: Grid) -> Position:
    x, y = zip(*grid)
    return (max(x), max(y))


def dijkstra(graph: Graph, start: Position, target: Position) -> int:
    queue: list[tuple[int, Position]] = [(0, start)]
    seen: set[Position] = set()
    mins = {start: 0}
    while queue:
        (cost, current) = heappop(queue)
        if current not in seen:
            seen.add(current)
            if current == target:
                return cost

            for to, value in graph.get(current, ()):
                if to in seen:
                    continue
                prev = mins.get(to)
                next = cost + value
                if prev is None or next < prev:
                    mins[to] = next
                    heappush(queue, (next, to))

    return int("inf")


def solve(grid: Grid, target: Position) -> int:
    graph: Graph = defaultdict(list)
    for position in grid.keys():
        for neighbor in get_neighbors(position):
            if neighbor in grid:
                graph[position].append((neighbor, grid[neighbor]))

    return dijkstra(graph, (0, 0), target)


def part_1(input: str) -> int:
    grid = parse_input(input)
    return solve(grid, grid_max(grid))


def expand_grid(grid: Grid, w: int, h: int) -> Grid:
    for x in range(w, w * 5):
        for y in range(h):
            grid[(x, y)] = grid.get((x, y), grid[(x - w, y)] % 9 + 1)

    for x in range(w * 5):
        for y in range(h, h * 5):
            grid[(x, y)] = grid.get((x, y), grid[(x, y - w)] % 9 + 1)

    return grid


def part_2(input: str) -> int:
    grid = parse_input(input)
    (w, h) = grid_max(grid)
    grid = expand_grid(grid, w + 1, h + 1)

    return solve(grid, grid_max(grid))


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


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 2907


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
