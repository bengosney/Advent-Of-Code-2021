# Standard Library
import os


def read_input(day: int) -> str:
    with open(os.path.join(os.path.dirname(__file__), "..", "inputs", f"day-{day:02}.txt")) as f:
        return f.read().strip().strip("\n\r")


def read_input_lines(day: int) -> list[str]:
    return read_input(day).split("\n")


# --- tests


def test_read_input():
    assert read_input(0) == """test1\ntest2"""


def test_read_input_lines():
    assert read_input_lines(0) == ["test1", "test2"]
