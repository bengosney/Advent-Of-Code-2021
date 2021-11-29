# Standard Library
import os


def getInput(day: int) -> str:
    with open(os.path.join(os.path.dirname(__file__), "..", "inputs", f"day-{day:02}.txt")) as f:
        return f.read().strip().strip("\n\r")


def getInputLines(day: int) -> list[str]:
    return getInput(day).split("\n")


# --- tests


def test_getInput():
    assert getInput(0) == """test1\ntest2"""


def test_getInputLines():
    assert getInputLines(0) == ["test1", "test2"]
