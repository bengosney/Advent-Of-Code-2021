# Standard Library
import os


def getInput(day: int) -> str:
    with open(os.path.join(os.path.dirname(__file__), "inputs", f"day-{day:02}.txt")) as f:
        return f.read().strip()
