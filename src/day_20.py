# Standard Library
from collections import defaultdict
from typing import Counter, Iterable

# First Party
from utils import read_input

Position = tuple[int, int]
Grid = dict[Position, str]


def get_neighbours(position: Position) -> Iterable[Position]:
    x, y = position

    for mod_y in [-1, 0, 1]:
        for mod_x in [-1, 0, 1]:
            yield (x + mod_x, y + mod_y)


def enhace(image: Grid, enhancement_algorithm: str) -> Grid:
    enhanced: Grid = defaultdict(lambda: ".")
    for position in full_range(image):
        binay = []
        for neighbour in get_neighbours(position):
            binay.append("1" if image[neighbour] == "#" else "0")
        dec = int("".join(binay), 2)
        enhanced[position] = enhancement_algorithm[dec]

    return enhanced


def minmax(image: Grid) -> tuple[tuple[int, int], tuple[int, int]]:
    filtered_image = {k: v for k, v in image.items() if v != "."}

    max_x = max(filtered_image.keys(), key=lambda x: x[0])[0]
    max_y = max(filtered_image.keys(), key=lambda x: x[1])[1]
    min_x = min(filtered_image.keys(), key=lambda x: x[0])[0]
    min_y = min(filtered_image.keys(), key=lambda x: x[1])[1]

    return (min_x, min_y), (max_x, max_y)


def full_range(image: Grid) -> Iterable[tuple[int, int]]:
    (min_x, min_y), (max_x, max_y) = minmax(image)

    extra = 1
    for x in range(min_x - extra, max_x + extra + 1):
        for y in range(min_y - extra, max_y + extra + 1):
            yield (x, y)


def draw(image: Grid):
    (min_x, min_y), (max_x, max_y) = minmax(image)
    extra = 1
    print()
    for y in range(min_y - extra, max_y + extra + 1):
        for x in range(min_x - extra, max_x + extra + 1):
            print(image[(x, y)], end="")
        print()
    print()


def part_1(input: str) -> int:
    enhancement_algorithm, raw_image = input.split("\n\n")
    image: Grid = defaultdict(lambda: ".")
    for y, row in enumerate(raw_image.split("\n")):
        for x, pixel in enumerate(row):
            image[(x, y)] = pixel

    # draw(image.copy())
    image = enhace(image.copy(), enhancement_algorithm)
    # draw(image.copy())
    image = enhace(image.copy(), enhancement_algorithm)
    # draw(image.copy())

    counter = Counter(image.values())
    return counter["#"]


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 35


# def test_part_2():
#     input = get_example_input()
#     assert part_2(input) is not None


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 5218


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
