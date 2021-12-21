# Standard Library
from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product

# First Party
from utils import read_input


class Dice:
    def __init__(self, size: int = 100):
        self.values = deque(range(1, size + 1))
        self.rolls = 0

    def roll(self) -> int:
        self.values.rotate(-1)
        self.rolls += 1
        return self.values[-1]


class Player:
    def __init__(self, name: str, start_position: int, winning_score: int, board_size: int = 10):
        self.name = name
        self.position = deque(range(1, board_size + 1))
        self.position.rotate(-(start_position - 1))
        self.score = 0
        self.winning_score = winning_score

    def __repr__(self):
        return f"Player {self.name} at {self.position[0]} with score {self.score}"

    def has_won(self):
        return self.score >= self.winning_score

    def roll(self, dice: Dice):
        self.move(-sum(dice.roll() for _ in range(3)))

    def move(self, by: int):
        self.position.rotate(by)
        self.score += self.position[0]


@dataclass(frozen=True)
class State:
    positions: tuple[int, int]
    scores: tuple[int, int]


@lru_cache(maxsize=None)
def get_rolls():
    return [sum(roll) for roll in list(product(range(1, 4), repeat=3))]


@lru_cache(maxsize=None)
def move(by: int, player: int, state: State) -> State:
    positions = list(state.positions)
    scores = list(state.scores)
    positions[player] = ((positions[player] + by - 1) % 10) + 1
    scores[player] += positions[player]

    return State((positions[0], positions[1]), (scores[0], scores[1]))


@lru_cache(maxsize=None)
def play(player: int, state: State) -> tuple[int, int]:
    if state.scores[0] >= 21:
        return (1, 0)
    if state.scores[1] >= 21:
        return (0, 1)

    socres = [0, 0]
    for roll in get_rolls():
        moved = move(roll, player, state)
        results = play(1 if player == 0 else 0, moved)
        socres[0] += results[0]
        socres[1] += results[1]

    return socres[0], socres[1]


def part_2(input: str) -> int:
    lines = input.splitlines()
    p1 = int(lines[0][-1])
    p2 = int(lines[1][-1])

    scores = play(0, State((p1, p2), (0, 0)))

    return max(scores)


def part_1(input: str) -> int:
    lines = input.splitlines()
    player1 = Player("1", int(lines[0][-1]), 1000)
    player2 = Player("2", int(lines[1][-1]), 1000)

    players = deque([player1, player2])
    dice = Dice()

    while True:
        player = players[0]
        players.rotate(1)

        player.roll(dice)
        if player.has_won():
            break

    return players[0].score * dice.rolls


# -- Tests


def test_deterministic_dice_rolls():
    dice = Dice(6)
    for _ in range(3):
        for i in range(1, 7):
            assert dice.roll() == i


def get_example_input() -> str:
    return """Player 1 starting position: 4
Player 2 starting position: 8"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 739785


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 444356092776315


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 916083


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
