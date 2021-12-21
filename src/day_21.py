# Standard Library
from collections import deque

# First Party
from utils import read_input


class Dice:
    def roll(self) -> int:
        raise NotImplementedError


class DeterministicDice(Dice):
    def __init__(self, size: int = 100):
        self.values = deque(range(1, size + 1))
        self.rolls = 0

    def roll(self) -> int:
        self.values.rotate(-1)
        self.rolls += 1
        return self.values[-1]


class Player:
    def __init__(self, name: str, start_position: int, board_size: int = 10):
        self.name = name
        self.position = deque(range(1, board_size + 1))
        self.position.rotate(-(start_position - 1))
        self.score = 0

    def __repr__(self):
        return f"Player {self.name} at {self.position[0]} with score {self.score} and {self.moves} moves"

    def has_won(self):
        return self.score >= 1000

    def move(self, dice: Dice):
        self.position.rotate(-sum(dice.roll() for _ in range(3)))
        self.score += self.position[0]


def part_1(input: str) -> int:
    lines = input.splitlines()
    player1 = Player("1", int(lines[0][-1]))
    player2 = Player("2", int(lines[1][-1]))

    players = deque([player1, player2])
    dice = DeterministicDice()

    while True:
        player = players[0]
        players.rotate(1)

        player.move(dice)
        if player.has_won():
            break

    return players[0].score * dice.rolls


def part_2(input: str) -> int:
    pass


# -- Tests


def test_deterministic_dice_rolls():
    dice = DeterministicDice(6)
    for _ in range(3):
        for i in range(1, 7):
            assert dice.roll() == i


def get_example_input() -> str:
    return """Player 1 starting position: 4
Player 2 starting position: 8"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 739785


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
