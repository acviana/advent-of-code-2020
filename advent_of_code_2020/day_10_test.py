from advent_of_code_2020.day_10 import (
    calc_differences,
    calc_all_paths,
    parse_data,
)


TEST_DATA = """16
10
15
5
1
11
7
19
6
12
4"""
TEST_DATA = [item for item in TEST_DATA.split("\n")]
TEST_PARSED_DATA = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

TEST_DATA_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
TEST_DATA_2 = [item for item in TEST_DATA_2.split("\n")]


def test_parse_data():
    assert parse_data(TEST_DATA) == TEST_PARSED_DATA


def test_calc_differences():
    assert calc_differences(TEST_PARSED_DATA) == [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]


def test_calc_options():
    calc_all_paths(TEST_PARSED_DATA) == 8
    calc_all_paths(parse_data(TEST_DATA_2)) == 19208
