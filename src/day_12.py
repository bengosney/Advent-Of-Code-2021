# Standard Library
import multiprocessing as mp
from functools import partial
from itertools import chain, combinations

# First Party
from utils import read_input


class node:
    BIG = "big"
    SMALL = "small"
    SPECIAL = "special"

    def __init__(self, name) -> None:
        self.name = name
        self.links: set["node"] = set()
        self.size = self.BIG if ord(name[0]) < 97 else self.SMALL

    @classmethod
    def build(cls, lines: list[str]) -> dict[str, "node"]:
        nodes: dict[str, "node"] = {}
        for line in lines:
            names = line.split("-")
            for name in names:
                nodes[name] = nodes.get(name, cls(name))

            for name1, name2 in combinations(names, 2):
                nodes[name1].link(nodes[name2])

        return nodes

    def link(self, other):
        self.links.add(other)
        other.links.add(self)

    def __str__(self) -> str:
        return self.name

    @property
    def type(self) -> str:
        if self.name in ["start", "end"]:
            return self.SPECIAL

        return self.size

    def walk(self, visited: list["node"] = [], can_revisit: str | None = None) -> list[str]:
        if self.name == "end":
            return [self.name]

        if self in visited:
            if self.name == can_revisit:
                can_revisit = None
            else:
                return []

        if self.size == "small":
            visited.append(self)

        paths = []
        for link in self.links:
            path = link.walk([*visited], can_revisit)
            if len(path):
                for p in path:
                    paths.append(f"{self.name} -> {p}")

        return paths


def part_1(input: str) -> int:
    lines = input.splitlines()
    nodes = node.build(lines)

    paths = nodes["start"].walk()

    return len(paths)


def walk(name, nodes):
    return nodes["start"].walk([], name)


def part_2(input: str) -> int:
    lines = input.splitlines()
    nodes = node.build(lines)

    walk_nodes = partial(walk, nodes=nodes)

    pool = mp.Pool(mp.cpu_count())
    paths = pool.map(walk_nodes, [n.name for n in nodes.values() if n.type == node.SMALL])

    return len(set(chain.from_iterable(paths)))


# -- Tests


def get_example_input() -> str:
    return """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def test_part_1():
    input = get_example_input()
    assert part_1(input) == 10


def test_part_2():
    input = get_example_input()
    assert part_2(input) == 36


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 4304


def test_part_2_real():
    input = read_input(__file__)
    assert part_2(input) == 118242


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
