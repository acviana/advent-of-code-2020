from advent_of_code_2020.day_10 import parse_data


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


def test_parse_data():
    print(parse_data(TEST_DATA))
