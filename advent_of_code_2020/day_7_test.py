from advent_of_code_2020.day_7 import (
    check_color,
    count_containing_bags,
    parse_data,
)


TEST_DATA = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""

TEST_PARSED_DATA = {
    "bright white": {"shiny gold": 1},
    "dark olive": {"dotted black": 4, "faded blue": 3},
    "dark orange": {"bright white": 3, "muted yellow": 4},
    "dotted black": {},
    "faded blue": {},
    "light red": {"bright white": 1, "muted yellow": 2},
    "muted yellow": {"faded blue": 9, "shiny gold": 2},
    "shiny gold": {"dark olive": 1, "vibrant plum": 2},
    "vibrant plum": {"dotted black": 6, "faded blue": 5},
}


def test_parse_data():
    test_data = [item.strip() for item in TEST_DATA.split("\n")]
    test_result = parse_data(test_data)
    assert TEST_PARSED_DATA == test_result


def test_check_color():
    assert check_color(TEST_PARSED_DATA, "bright white", "shiny gold")
    assert not check_color(TEST_PARSED_DATA, "dark olive", "shiny gold")
    assert check_color(TEST_PARSED_DATA, "dark orange", "shiny gold")
    assert not check_color(TEST_PARSED_DATA, "dotted black", "shiny gold")
    assert not check_color(TEST_PARSED_DATA, "faded blue", "shiny gold")
    assert check_color(TEST_PARSED_DATA, "light red", "shiny gold")
    assert check_color(TEST_PARSED_DATA, "muted yellow", "shiny gold")
    assert not check_color(TEST_PARSED_DATA, "shiny gold", "shiny gold")
    assert not check_color(TEST_PARSED_DATA, "vibrant plum", "shiny gold")


def test_count_containing_bags():
    assert count_containing_bags(TEST_PARSED_DATA, "shiny gold")
