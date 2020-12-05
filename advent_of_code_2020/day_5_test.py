from advent_of_code_2020.day_5 import (
    binary_partition,
    parse_seat_instrcutions,
    get_seat_id,
)


def test_binary_partition():
    assert binary_partition("F", 0, 127) == {"bottom": 0, "top": 63}
    assert binary_partition("B", 0, 63) == {"bottom": 32, "top": 63}
    assert binary_partition("F", 32, 63) == {"bottom": 32, "top": 47}
    assert binary_partition("B", 32, 47) == {"bottom": 40, "top": 47}
    assert binary_partition("B", 40, 47) == {"bottom": 44, "top": 47}
    assert binary_partition("F", 44, 47) == {"bottom": 44, "top": 45}
    assert binary_partition("F", 44, 45) == {"bottom": 44, "top": 44}
    assert binary_partition("R", 0, 7) == {"bottom": 4, "top": 7}
    assert binary_partition("L", 4, 7) == {"bottom": 4, "top": 5}
    assert binary_partition("R", 4, 5) == {"bottom": 5, "top": 5}


def test_parse_seat_instrucionts():
    assert parse_seat_instrcutions("FBFBBFFRLR", 128)["top"] == 44
    assert parse_seat_instrcutions("RLR", 8)["top"] == 5


def test_get_seat_id():
    assert get_seat_id("FBFBBFFRLR") == 357
    assert get_seat_id("BFFFBBFRRR") == 567
    assert get_seat_id("FFFBBBFRRR") == 119
    assert get_seat_id("BBFFBBFRLL") == 820
