# First Party
from utils import read_input


def part_1(input: str) -> int:
    instructions = input.splitlines()

    position = 0
    depth = 0

    for instruction in instructions:
        cmd, amt = instruction.split(" ")
        match cmd:
            case "forward":
                position += int(amt)
            case "backward":
                position -= int(amt)
            case "up":
                depth -= int(amt)
            case "down":
                depth += int(amt)

    return position * depth


def part_2(input: str) -> int:
    instructions = input.splitlines()

    position = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        cmd, amt = instruction.split(" ")
        match cmd:
            case "forward":
                position += int(amt)
                depth -= int(amt) * aim
            case "backward":
                position -= int(amt)
                depth += int(amt) * aim
            case "up":
                aim += int(amt)
            case "down":
                aim -= int(amt)

    return position * depth


# -- Tests


def get_example_input() -> str:
    return """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_part_1():
    assert part_1(get_example_input()) == 150


def test_part_2():
    assert part_2(get_example_input()) == 900


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 2019945


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1599311480


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
