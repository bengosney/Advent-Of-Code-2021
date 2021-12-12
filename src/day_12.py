# First Party
from utils import read_input

# Third Party
from icecream import ic


class node:
    def __init__(self, name) -> None:
        self.name = name
        self.links = set()
        self.size = "big" if ord(name[0]) < 97 else "small"

    @classmethod
    def build(cls, lines: list[str]) -> dict[str, "node"]:
        nodes = {}
        for line in lines:
            name1, name2 = line.split("-")
            if name1 not in nodes:
                nodes[name1] = node(name1)
            if name2 not in nodes:
                nodes[name2] = node(name2)
            nodes[name1].link(nodes[name2])

        return nodes

    def link(self, other):
        self.links.add(other)
        other.links.add(self)

    def __str__(self) -> str:
        return self.name

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


def part_2(input: str) -> int:
    lines = input.splitlines()
    nodes = node.build(lines)

    paths = []
    small_names = [n.name for n in nodes.values() if n.size == "small" and n.name not in ["start", "end"]]
    ic(small_names)
    for name in small_names:
        paths += nodes["start"].walk([], name)

    return len(set(paths))


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


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
