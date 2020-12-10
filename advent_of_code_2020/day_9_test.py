from advent_of_code_2020.day_9 import (
    check_valid_number,
    find_encryption_set,
    find_invalid_number,
)

TEST_DATA = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
TEST_DATA = [int(item) for item in TEST_DATA.split("\n")]


def test_check_valid_number():
    assert check_valid_number(range(1, 26), 26)
    assert check_valid_number(range(1, 26), 49)
    assert not check_valid_number(range(1, 26), 50)
    assert not check_valid_number(range(1, 26), 100)


def test_find_invalid_number():
    assert find_invalid_number(TEST_DATA, 5) == 127


def test_find_encrpytion_set():
    assert find_encryption_set(TEST_DATA, 127) == 62
