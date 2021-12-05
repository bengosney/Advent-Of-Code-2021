# Standard Library
from importlib import import_module
from pathlib import Path
from time import time

# First Party
from utils import read_input

# Third Party
from rich.console import Console
from rich.table import Table


def avg(lst: list[int | float]) -> float:
    return sum(lst) / len(lst)


def timeit(day: str, iterations: int = 1) -> tuple[float, float]:
    module = import_module(day)
    input = read_input(day)

    part_1_times: list[float] = []
    for _ in range(iterations):
        start = time()
        module.part_1(input)
        part_1_times.append(time() - start)

    part_2_times: list[float] = []
    for _ in range(iterations):
        start = time()
        module.part_2(input)
        part_2_times.append(time() - start)

    return avg(part_1_times), avg(part_2_times)


def time_everything():
    table = Table(title="AOC 2021 - Timings")

    table.add_column("Day", justify="left", style="bold")
    table.add_column("Part 1", justify="right")
    table.add_column("Part 2", justify="right")

    for path in sorted(Path("./src").glob("day_*.py")):
        day = path.name.replace(".py", "")
        p1, p2 = timeit(path.name.replace(".py", ""))

        _, d = day.split("_")
        table.add_row(f"{int(d)}", f"{p1:.3f}s", f"{p2:.3f}s")

    console = Console()
    console.print(table)


if __name__ == "__main__":
    time_everything()
