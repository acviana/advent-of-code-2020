from collections import Counter

from advent_of_code_2020.day_11 import (
    count_occupied_seats,
    get_data_slice,
    get_final_state,
    get_neighbors,
    get_next_data_set,
    get_next_state,
)

TEST_DATA_1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
TEST_DATA_1 = [item.strip() for item in TEST_DATA_1.split("\n")]

TEST_DATA_2 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
TEST_DATA_2 = [item.strip() for item in TEST_DATA_2.split("\n")]

TEST_DATA_3 = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
TEST_DATA_3 = [item.strip() for item in TEST_DATA_3.split("\n")]

TEST_DATA_FINAL = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
TEST_DATA_FINAL = [item.strip() for item in TEST_DATA_FINAL.split("\n")]


def test_get_data_slice():
    assert get_data_slice(5, 5, TEST_DATA_1) == ['.LL', 'LLL', 'L..']
    assert get_data_slice(0, 0, TEST_DATA_1) == ['L.', 'LL']
    assert get_data_slice(0, 9, TEST_DATA_1) == ['LL', 'LL']
    assert get_data_slice(9, 0, TEST_DATA_1) == ['L.', 'L.']
    assert get_data_slice(9, 9, TEST_DATA_1) == ['.L', 'LL']


def test_get_neighbors():
    assert get_neighbors(get_data_slice(5, 5, TEST_DATA_1), TEST_DATA_1[5][5]) == Counter({'L': 5, '.': 3})
    assert get_neighbors(get_data_slice(0, 0, TEST_DATA_1), TEST_DATA_1[0][0]) == Counter({'L': 2, '.': 1})
    assert get_neighbors(get_data_slice(0, 9, TEST_DATA_1), TEST_DATA_1[0][9]) == Counter({'L': 3})
    assert get_neighbors(get_data_slice(9, 0, TEST_DATA_1), TEST_DATA_1[9][0]) == Counter({'.': 2, 'L': 1})
    assert get_neighbors(get_data_slice(9, 9, TEST_DATA_1), TEST_DATA_1[9][9]) == Counter({'L': 2, '.': 1})


def test_get_next_state():
    assert get_next_state(5, 5, TEST_DATA_1) == "#"
    assert get_next_state(0, 0, TEST_DATA_1) == "#"
    assert get_next_state(0, 9, TEST_DATA_1) == "#"
    assert get_next_state(9, 0, TEST_DATA_1) == "#"
    assert get_next_state(9, 9, TEST_DATA_1) == "#"


def test_get_next_data_set():
    assert get_next_data_set(TEST_DATA_1) == TEST_DATA_2
    assert get_next_data_set(TEST_DATA_2) == TEST_DATA_3


def test_get_final_state():
    assert get_final_state(TEST_DATA_1) == TEST_DATA_FINAL


def test_count_occupied_seats():
    final_state = get_final_state(TEST_DATA_1)
    assert count_occupied_seats(final_state) == 37
