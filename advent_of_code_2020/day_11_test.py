from collections import Counter

from advent_of_code_2020.day_11 import (
    count_occupied_seats,
    get_data_slice,
    get_final_state,
    get_line_of_sight,
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

TEST_DATA_EXAMPLE_1_LOS = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
TEST_DATA_EXAMPLE_1_LOS = [item.strip() for item in TEST_DATA_EXAMPLE_1_LOS.split("\n")]

TEST_DATA_EXAMPLE_2_LOS = """.............
.L.L.#.#.#.#.
............."""
TEST_DATA_EXAMPLE_2_LOS = [item.strip() for item in TEST_DATA_EXAMPLE_2_LOS.split("\n")]

TEST_DATA_EXAMPLE_3_LOS = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
TEST_DATA_EXAMPLE_3_LOS = [item.strip() for item in TEST_DATA_EXAMPLE_3_LOS.split("\n")]

TEST_DATA_3_LOS = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
TEST_DATA_3_LOS = [item.strip() for item in TEST_DATA_3_LOS.split("\n")]

TEST_DATA_4_LOS = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
TEST_DATA_4_LOS = [item.strip() for item in TEST_DATA_4_LOS.split("\n")]


TEST_DATA_FINAL_LOS = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""
TEST_DATA_FINAL_LOS = [item.strip() for item in TEST_DATA_FINAL_LOS.split("\n")]


def test_get_line_of_sight():
    assert get_line_of_sight(4, 3, 1, 0, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, -1, 0, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, 0, 1, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, 0, -1, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, 1, 1, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, 1, -1, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, -1, 1, TEST_DATA_EXAMPLE_1_LOS) == "#"
    assert get_line_of_sight(4, 3, -1, -1, TEST_DATA_EXAMPLE_1_LOS) == "#"

    assert get_line_of_sight(0, 0, 1, 0, TEST_DATA_2) == "#"
    assert get_line_of_sight(0, 0, -1, 0, TEST_DATA_2) == ""
    assert get_line_of_sight(0, 0, 0, 1, TEST_DATA_2) == "#"
    assert get_line_of_sight(0, 0, 0, -1, TEST_DATA_2) == ""
    assert get_line_of_sight(0, 0, 1, 1, TEST_DATA_2) == "#"
    assert get_line_of_sight(0, 0, 1, -1, TEST_DATA_2) == ""
    assert get_line_of_sight(0, 0, -1, 1, TEST_DATA_2) == ""
    assert get_line_of_sight(0, 0, -1, -1, TEST_DATA_2) == ""


def test_get_data_slice():
    assert get_data_slice(5, 5, TEST_DATA_1, "nearest_neighbors") == [
        ".LL",
        "LLL",
        "L..",
    ]
    assert get_data_slice(0, 0, TEST_DATA_1, "nearest_neighbors") == ["L.", "LL"]
    assert get_data_slice(0, 9, TEST_DATA_1, "nearest_neighbors") == ["LL", "LL"]
    assert get_data_slice(9, 0, TEST_DATA_1, "nearest_neighbors") == ["L.", "L."]
    assert get_data_slice(9, 9, TEST_DATA_1, "nearest_neighbors") == [".L", "LL"]

    expected_result = ["#", "#", "#", "#", "#", "#", "#", "#", "L"]
    assert (
        get_data_slice(4, 3, TEST_DATA_EXAMPLE_1_LOS, "line_of_sight")
        == expected_result
    )

    assert get_data_slice(0, 0, TEST_DATA_2, "line_of_sight") == ["#", "#", "#", "#"]
    assert get_data_slice(2, 0, TEST_DATA_2, "line_of_sight") == [
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
    ]


def test_get_neighbors():
    assert get_neighbors(
        get_data_slice(5, 5, TEST_DATA_1, "nearest_neighbors"), TEST_DATA_1[5][5]
    ) == Counter({"L": 5, ".": 3})
    assert get_neighbors(
        get_data_slice(0, 0, TEST_DATA_1, "nearest_neighbors"), TEST_DATA_1[0][0]
    ) == Counter({"L": 2, ".": 1})
    assert get_neighbors(
        get_data_slice(0, 9, TEST_DATA_1, "nearest_neighbors"), TEST_DATA_1[0][9]
    ) == Counter({"L": 3})
    assert get_neighbors(
        get_data_slice(9, 0, TEST_DATA_1, "nearest_neighbors"), TEST_DATA_1[9][0]
    ) == Counter({".": 2, "L": 1})
    assert get_neighbors(
        get_data_slice(9, 9, TEST_DATA_1, "nearest_neighbors"), TEST_DATA_1[9][9]
    ) == Counter({"L": 2, ".": 1})

    assert (
        get_neighbors(
            get_data_slice(4, 3, TEST_DATA_EXAMPLE_1_LOS, "line_of_sight"),
            TEST_DATA_EXAMPLE_1_LOS[4][3],
        )
        == Counter({"#": 8, "L": 0})
    )

    assert (
        get_neighbors(
            get_data_slice(1, 1, TEST_DATA_EXAMPLE_2_LOS, "line_of_sight"),
            TEST_DATA_EXAMPLE_2_LOS[1][1],
        )
        == Counter({".": 7, "L": 1})
    )

    assert (
        get_neighbors(
            get_data_slice(3, 3, TEST_DATA_EXAMPLE_3_LOS, "line_of_sight"),
            TEST_DATA_EXAMPLE_3_LOS[3][3],
        )
        == Counter({".": 8, "L": 0})
    )


def test_get_next_state():
    assert get_next_state(5, 5, TEST_DATA_1, "nearest_neighbors") == "#"
    assert get_next_state(0, 0, TEST_DATA_1, "nearest_neighbors") == "#"
    assert get_next_state(0, 9, TEST_DATA_1, "nearest_neighbors") == "#"
    assert get_next_state(9, 0, TEST_DATA_1, "nearest_neighbors") == "#"
    assert get_next_state(9, 9, TEST_DATA_1, "nearest_neighbors") == "#"

    assert get_next_state(2, 0, TEST_DATA_2, "line_of_sight") == "L"
    assert get_next_state(1, 0, TEST_DATA_2, "line_of_sight") == "#"


def test_get_next_data_set():
    assert get_next_data_set(TEST_DATA_1, "nearest_neighbors") == TEST_DATA_2
    assert get_next_data_set(TEST_DATA_2, "nearest_neighbors") == TEST_DATA_3

    assert get_next_data_set(TEST_DATA_1, "line_of_sight") == TEST_DATA_2
    assert get_next_data_set(TEST_DATA_2, "line_of_sight") == TEST_DATA_3_LOS


def test_get_final_state():
    assert get_final_state(TEST_DATA_1, "nearest_neighbors") == TEST_DATA_FINAL
    assert get_final_state(TEST_DATA_1, "line_of_sight") == TEST_DATA_FINAL_LOS


def test_count_occupied_seats():
    final_state = get_final_state(TEST_DATA_1, "nearest_neighbors")
    assert count_occupied_seats(final_state) == 37
