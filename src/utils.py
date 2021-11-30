# Standard Library
import os


def read_input(day: str) -> str:
    file = os.path.splitext(os.path.basename(day))[0]
    with open(os.path.join(os.path.dirname(__file__), "..", "inputs", f"{file}.txt")) as f:
        return f.read().strip().strip("\n\r")


# --- tests


def test_read_input():
    assert read_input("day_00.py") == """test1\ntest2"""
