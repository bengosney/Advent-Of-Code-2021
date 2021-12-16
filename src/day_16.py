# Standard Library
from dataclasses import dataclass
from itertools import chain

# First Party
from utils import read_input

# Third Party
from icecream import ic


@dataclass
class Packet:
    version: int
    type: int
    value: int | None = None


@dataclass
class Litral(Packet):
    pass


class Operator(Packet):
    pass


def decode_packet(to_decode: str) -> tuple[list[Packet], str]:
    version = int(to_decode[0:3], 2)
    type_ = int(to_decode[3:6], 2)
    data = to_decode[6:]

    if type_ == 4:
        parts = []

        while True:
            is_last = data[0] == "0"
            parts.append(data[1:5])
            data = data[5:]
            if is_last:
                break

        value = int("".join(parts), 2)
        return [Litral(version, type_, value)], data

    type_length = 15 if data[0] == "0" else 11
    length = int(data[1 : type_length + 1], 2)

    if type_length == 15:
        sub_packet_data = data[type_length + 1 : type_length + 1 + length]
        sub_packets: list[Packet] = [Operator(version, type_)]
        while len(sub_packet_data):
            sub_packet, sub_packet_data = decode_packet(sub_packet_data)
            sub_packets = list(chain(sub_packets, sub_packet))
        return sub_packets, data[type_length + 1 + length :]
    else:
        sub_packets: list[Packet] = [Operator(version, type_)]
        sub_packet_data = data[type_length + 1 :]
        for _ in range(length):
            sub_packet, sub_packet_data = decode_packet(sub_packet_data)
            sub_packets = list(chain(sub_packets, sub_packet))
        return sub_packets, sub_packet_data


def hex_to_bin(input: str) -> str:
    return (bin(int(input, 16))[2:]).zfill(len(input) * 4)


def part_1(input: str) -> int:
    bin_packet = hex_to_bin(input)
    ic(bin_packet)
    packets, _ = decode_packet(bin_packet)
    ver_count = 0
    for packet in packets:
        ver_count += packet.version

    return ver_count


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> list[tuple[str, int]]:
    return [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ]


def test_part_1():
    input = get_example_input()
    for hex, val in input:
        assert part_1(hex) == val


def test_packet_litral():
    packets, _ = decode_packet(hex_to_bin("D2FE28"))
    assert len(packets) == 1
    assert packets[0] == Litral(6, 4, 2021)


def test_packet_15bit_op():
    packets, _ = decode_packet(hex_to_bin("38006F45291200"))

    assert len(packets) == 3

    assert packets[0] == Operator(1, 6)

    assert packets[1] == Litral(6, 4, 10)
    assert packets[2] == Litral(2, 4, 20)


def test_packet_11bit_op():
    packets, _ = decode_packet(hex_to_bin("EE00D40C823060"))

    assert len(packets) == 4

    assert packets[0] == Operator(7, 3)

    assert packets[1] == Litral(2, 4, 1)
    assert packets[2] == Litral(4, 4, 2)
    assert packets[3] == Litral(1, 4, 3)


# def test_part_2():
#     input = get_example_input()
#     assert part_2(input) is not None


def test_part_1_real():
    input = read_input(__file__)
    assert part_1(input) == 965


# def test_part_2_real():
#     input = read_input(__file__)
#     assert part_2(input) is not None


# -- Main

if __name__ == "__main__":
    input = read_input(__file__)

    print(f"Part1: {part_1(input)}")
    print(f"Part2: {part_2(input)}")
