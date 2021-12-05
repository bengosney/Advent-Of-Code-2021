# Standard Library
from importlib import import_module
from pathlib import Path
from time import time
from typing import Callable

# First Party
from utils import read_input

# Third Party
import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table


def avg(lst: list[int | float]) -> float:
    return sum(lst) / len(lst)


def timeit(day: str, iterations: int = 1, progress: Callable | None = None) -> tuple[float, float]:
    module = import_module(day)
    input = read_input(day)

    part_1_times: list[float] = []
    for _ in range(iterations):
        start = time()
        module.part_1(input)  # type: ignore
        part_1_times.append(time() - start)
        if progress is not None:
            progress()

    part_2_times: list[float] = []
    for _ in range(iterations):
        start = time()
        module.part_2(input)  # type: ignore
        part_2_times.append(time() - start)
        if progress is not None:
            progress()

    return avg(part_1_times), avg(part_2_times)


@click.command()
@click.option("--iterations", "-i", default=10, help="Number of times to run each part")
def time_everything(iterations: int = 10) -> None:
    table = Table(title=f"AOC 2021 - Timings\n({iterations} iterations)")

    table.add_column("Day", justify="center", style="bold")
    table.add_column("Part 1", justify="right")
    table.add_column("Part 2", justify="right")

    days = list(Path("./src").glob("day_*.py"))

    with Progress(transient=True) as progress:
        p = progress.add_task("Running code", total=(len(days) * 2) * iterations)
        for path in sorted(days):
            day = path.name.replace(".py", "")
            p1, p2 = timeit(day, iterations, lambda: progress.update(p, advance=1))

            _, d = day.split("_")
            table.add_row(f"{int(d)}", f"{p1:.3f}s", f"{p2:.3f}s")
            progress.update(p, advance=1)

    with Console() as console:
        console.print(Panel(table, expand=False))


if __name__ == "__main__":
    time_everything()
