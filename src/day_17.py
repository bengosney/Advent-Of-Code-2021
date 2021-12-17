# Standard Library
import re
from functools import lru_cache
from typing import Iterable

# First Party
from utils import read_input

Vector = tuple[int, int]
Position = Vector
Target = tuple[Position, Position]


@lru_cache(maxsize=None)
def parse_input(input: str) -> Target:
    regex = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"

    matches = re.finditer(regex, input, re.MULTILINE)
    for match in matches:
        x1, x2, y1, y2 = match.groups()

        return (min(int(x1), int(x2)), max(int(y1), int(y2))), (max(int(x1), int(x2)), min(int(y1), int(y2)))

    raise Exception("No match")


@lru_cache(maxsize=None)
def get_ranges(target: Target) -> tuple[Iterable[int], Iterable[int]]:
    (x1, y1), (x2, y2) = target

    return range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)


@lru_cache(maxsize=None)
def is_in(position: Position, target: Target) -> bool:
    x, y = position
    x_range, y_range = get_ranges(target)

    return x in x_range and y in y_range


@lru_cache(maxsize=None)
def is_past(position: Position, target: Target) -> bool:
    x, y = position
    _, (x2, y2) = target

    return x > x2 or y < y2


@lru_cache(maxsize=None)
def move(position: Position, direction: Vector) -> tuple[Position, Vector]:
    x, y = position
    dx, dy = direction

    return (x + dx, y + dy), (max(0, (dx - 1)), (dy - 1))


def does_hit(start: Vector, target: Target) -> bool:
    position: Position = (0, 0)
    direction: Vector = start

    while not is_past(position, target):
        if is_in(position, target):
            return True

        position, direction = move(position, direction)

    return False


def part_1(input: str) -> int:
    target = parse_input(input)
    _, (_, max_y) = target

    y = abs(max_y)

    return int(y * ((y - 1) / 2))


def get_all_hits(input: str) -> Iterable[Position]:
    target = parse_input(input)
    _, (max_x, _) = target

    max_y = part_1(input) + 1

    for x in range(max_x + 1):
        for y in range(-max_y, max_y):
            if does_hit((x, y), target):
                yield (x, y)


def part_2(input: str) -> int:
    hits = get_all_hits(input)

    return len(list(hits))


# -- Tests


def get_example_input() -> str:
    return "target area: x=20..30, y=-10..-5"


def test_parse_input():
    input = get_example_input()
    assert parse_input(input) == ((20, -5), (30, -10))


def test_24_m5():
    input = get_example_input()
    target = parse_input(input)
    assert does_hit((24, -5), target) is True


def test_is_in_in():
    target = ((10, 10), (30, 30))
    assert is_in((15, 15), target) is True


def test_is_in_out():
    target = ((10, 10), (30, 30))
    assert is_in((45, 45), target) is False


def test_is_past_before():
    target = ((10, -10), (30, -30))
    assert is_past((5, 5), target) is False


def test_is_past_in():
    target = ((10, -10), (30, -30))
    assert is_past((15, -15), target) is False


def test_is_past_after():
    target = ((10, -10), (30, -30))
    assert is_past((45, -45), target) is True


def test_does_hit_hit():
    target = parse_input(get_example_input())
    assert does_hit((7, 2), target) is True


def get_all_test_hits():
    return [
        (24, -5),
        (28, -7),
        (21, -6),
        (14, -3),
        (25, -8),
        (23, -7),
        (27, -6),
        (7, 4),
        (6, 5),
        (13, -3),
        (21, -5),
        (29, -5),
        (27, -7),
        (6, 3),
        (14, -4),
        (30, -10),
        (26, -8),
        (24, -6),
        (22, -10),
        (26, -9),
        (22, -9),
        (29, -7),
        (6, 6),
        (6, 9),
        (9, 0),
        (29, -10),
        (6, 1),
        (20, -7),
        (22, -5),
        (12, -3),
        (6, 0),
        (12, -4),
        (26, -5),
        (14, -2),
        (7, 9),
        (20, -6),
        (21, -7),
        (20, -5),
        (6, 4),
        (6, 2),
        (15, -3),
        (28, -9),
        (23, -9),
        (11, -4),
        (10, -1),
        (20, -9),
        (21, -10),
        (24, -9),
        (22, -6),
        (11, -2),
        (6, 7),
        (21, -9),
        (29, -9),
        (12, -2),
        (7, 1),
        (28, -6),
        (9, -1),
        (11, -1),
        (28, -5),
        (22, -7),
        (29, -6),
        (6, 8),
        (20, -10),
        (8, -1),
        (28, -8),
        (15, -2),
        (26, -7),
        (7, 6),
        (7, 0),
        (10, -2),
        (30, -7),
        (21, -8),
        (24, -7),
        (27, -5),
        (25, -5),
        (29, -8),
        (7, 7),
        (7, 3),
        (9, -2),
        (11, -3),
        (13, -4),
        (30, -8),
        (28, -10),
        (27, -9),
        (30, -9),
        (30, -5),
        (25, -9),
        (26, -6),
        (30, -6),
        (7, -1),
        (13, -2),
        (15, -4),
        (7, 8),
        (22, -8),
        (23, -8),
        (23, -6),
        (24, -8),
        (7, 2),
        (27, -8),
        (23, -10),
        (25, -7),
        (8, 0),
        (26, -10),
        (20, -8),
        (25, -6),
        (25, -10),
        (8, 1),
        (24, -10),
        (7, 5),
        (23, -5),
        (27, -10),
        (8, -2),
    ]


def test_get_all_hits_hits():
    all_hits = list(get_all_hits(get_example_input()))
    part_2_matches = get_all_test_hits()
    for hit in part_2_matches:
        assert hit not in all_hits


def test_get_all_hits_misses():
    all_hits = list(get_all_hits(get_example_input()))
    part_2_matches = get_all_test_hits()
    for hit in all_hits:
        assert hit not in part_2_matches


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 45


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 112


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 9870


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
