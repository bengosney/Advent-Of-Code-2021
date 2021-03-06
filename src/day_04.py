# Standard Library
from collections import defaultdict

# First Party
from utils import read_input


class Board:
    def __init__(self, input: str) -> None:
        self.grid: dict[tuple[int, int], bool] = defaultdict(lambda: False)
        self.mapping: dict[int, tuple[int, int]] = {}
        self.unmarked: list[int] = []
        self.size: tuple[int, int] = (0, 0)

        for y, row in enumerate(input.replace("  ", " ").strip().split("\n")):
            for x, cell in enumerate(row.strip(" ").split(" ")):
                self.mapping[int(cell)] = (x, y)
                self.unmarked.append(int(cell))
                self.size = (max(self.size[0], x + 1), max(self.size[1], x + 1))

    @staticmethod
    def preparGame(input: str) -> tuple[list[int], list["Board"]]:
        split = input.split("\n\n")
        draw = list(map(int, split[0].split(",")))

        boards = [Board(b.replace("  ", " ")) for b in split[1:]]

        return draw, boards

    def set(self, num: int) -> None:
        if num in self.mapping:
            self.grid[self.mapping[num]] = True
            self.unmarked.remove(num)

    def bingoRow(self) -> bool:
        width, height = self.size
        return any(all(self.grid[(x, y)] for x in range(width)) for y in range(height))

    def bingoCol(self) -> bool:
        width, height = self.size
        return any(all(self.grid[(x, y)] for y in range(height)) for x in range(width))

    def bingo(self) -> bool:
        return self.bingoRow() or self.bingoCol()

    def score(self, draw: int) -> int:
        return draw * sum(self.unmarked)


def part_1(input: str) -> int:
    draw, boards = Board.preparGame(input)

    for d in draw:
        for b in boards:
            b.set(d)
            if b.bingo():
                return b.score(d)

    raise Exception("No bingo")


def part_2(input: str) -> int:
    draw, boards = Board.preparGame(input)

    for d in draw:
        won = []
        for k, b in enumerate(boards):
            b.set(d)
            if b.bingo():
                won.append(k)

        for k, b in enumerate(boards):
            if b.bingo():
                if len(boards) == 1:
                    return b.score(d)
                del boards[k]

    raise Exception("No bingo")


# -- Tests


def get_example_input() -> str:
    return """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_part_1():
    assert part_1(get_example_input()) == 4512


def test_part_1_real_fail():
    assert part_1(read_input(__file__)) < 4380


def test_part_2():
    assert part_2(get_example_input()) == 1924


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 2496


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 25925


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
