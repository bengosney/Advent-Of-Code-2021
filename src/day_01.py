# First Party
from utils import read_input
from icecream import ic

def part_1(input):
    previous = None
    count = 0
    for line in input.splitlines():
        line = int(line)
        if previous is None:
            previous = line
            continue
        if line > previous:
            count += 1
        previous = line
    return count

def part_2(input):
    splitinput = input.splitlines()
    newinput = [
        str(
            int(splitinput[i])
            + int(splitinput[i + 1])
            + int(splitinput[i + 2])
        )
        for i in range(len(splitinput) - 2)
    ]
    return part_1("\n".join(newinput))

# -- Tests


def test_part_1():
    example_input = """199
200
208
210
200
207
240
269
260
263"""
    assert part_1(example_input) == 7


def test_part_2():
    example_input = """199
200
208
210
200
207
240
269
260
263"""
    assert part_2(example_input) == 5


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 1688
    
def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 1728

# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
