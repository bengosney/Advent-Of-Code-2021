# Standard Library
import os
from typing import Iterable


def read_input(day: str) -> str:
    file = os.path.splitext(os.path.basename(day))[0]
    with open(os.path.join(os.path.dirname(__file__), "..", "inputs", f"{file}.txt")) as f:
        return f.read().strip().strip("\n\r")


def input_to_ints(input: str) -> list[int]:
    return [int(x) for x in input.split("\n")]


def ints_to_input(ints: Iterable[int]) -> str:
    return "\n".join([str(x) for x in ints])


# --- tests


def test_read_input():
    assert read_input("day_00.py") == "123\n456\n012"


def test_input_to_ints():
    input = read_input("day_00.py")
    assert input_to_ints(input) == [123, 456, 12]


def test_ints_to_input():
    ints = [123, 456, 12]
    assert ints_to_input(ints) == "123\n456\n12"
