# Standard Library
from collections import defaultdict

# First Party
from utils import read_input

# Third Party
from icecream import ic
from rich import print


class Board:
    def __init__(self, input: str) -> None:
        self.grid = defaultdict(lambda: False)
        self.mapping = {}
        self.revmapping = {}
        self.unmarked = []
        self.marked = []
        self.width = 0
        self.height = 0
        self.lastSet = None
        for y, row in enumerate(input.replace("  ", " ").split("\n")):
            for x, cell in enumerate(row.strip(" ").split(" ")):
                if cell != "":
                    self.mapping[int(cell)] = (x, y)
                    self.revmapping[(x, y)] = int(cell)
                    self.unmarked.append(int(cell))
                    self.width = 5  # max(self.width, x)
                    self.height = 5  # max(self.height+1, y)

    def set(self, num: int) -> bool:
        if num in self.mapping:
            self.grid[self.mapping[num]] = True
            self.marked.append(num)
            self.unmarked.remove(num)
            self.lastSet = num

            return True

        return False

    def bingoRow(self) -> bool:
        return any(all(self.grid[(x, y)] for x in range(self.width)) for y in range(self.height))

    def bingoCol(self) -> bool:
        return any(all(self.grid[(x, y)] for y in range(self.height)) for x in range(self.width))

    def bingo(self) -> bool:
        return self.bingoRow() or self.bingoCol()

    def score(self) -> int:
        if self.lastSet is None:
            raise Exception("No last set")
        ic(self.unmarked)
        return self.lastSet * sum(self.unmarked)

    def __str__(self) -> str:
        rep = f"Draw: {self.lastSet}\n"
        for y in range(self.height):
            for x in range(self.width):
                rep += f"{self.revmapping.get((x,y), '')}".rjust(3)
                rep += "|" if self.grid[(x, y)] else "."

            rep += "\n"

        return rep


def part_1(input: str) -> int:
    split = input.split("\n\n")
    draw = split[0].split(",")

    boards = [Board(b.replace("  ", " ")) for b in split[1:]]

    for d in draw:
        for b in boards:
            b.set(int(d))
            if b.bingo():
                print(b)
                return b.score()
    return 0


def part_2(input: str) -> int:
    split = input.split("\n\n")
    draw = split[0].split(",")

    boards = [Board(b.replace("  ", " ")) for b in split[1:]]

    for d in draw:
        for k, b in enumerate(boards):
            b.set(int(d))

        for k, b in enumerate(boards):
            if b.bingo():
                if len(boards) == 1:
                    print(",".join(draw))
                    print(b)
                    return b.score()
                del boards[k]

    return 0


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
