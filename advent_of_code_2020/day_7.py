from collections import ChainMap
from typing import Dict, List


def load_data() -> List[str]:
    with open("inputs/day_7_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def parse_allowed_contents(allowed_contents: str) -> Dict[str, int]:
    try:
        return {
            f"{item[1]} {item[2]}": int(item[0])
            for item in [item.split() for item in allowed_contents.split(",")]
        }
    except ValueError:
        # "no other bags." case
        return {}


def parse_rule(rule: str) -> Dict[str, Dict[str, int]]:
    bag_color, allowed_contents = rule.split(" bags contain ")
    return {bag_color: parse_allowed_contents(allowed_contents)}


def parse_data(data: List[str]) -> Dict[str, Dict[str, int]]:
    return dict(ChainMap(*[parse_rule(item) for item in data]))


def check_color(data: Dict[str, Dict[str, int]], key: str, search_term: str) -> bool:
    if data[key] == {}:
        return False
    if search_term in data[key]:
        return True
    else:
        return (
            True
            if True in [check_color(data, item, search_term) for item in data[key]]
            else False
        )


def sum_tree(data: Dict[str, Dict[str, int]], key: str) -> int:
    if data[key] == {}:
        return 1
    else:
        return sum([(data[key][item] * sum_tree(data, item)) for item in data[key]]) + 1


def count_possible_bag_colors(data: Dict[str, Dict[str, int]], color: str) -> int:
    return sum([check_color(data, item, color) for item in data])


def main() -> None:
    data = load_data()
    print(f"Loaded {len(data)} rules")
    parsed_data = parse_data(data)
    result = count_possible_bag_colors(parsed_data, "shiny gold")
    print(f"Found {result} bags that can contain 'shiny gold' bags")

    total_nested_bags = sum_tree(parsed_data, "shiny gold") - 1
    print(f"Found {total_nested_bags} total nested bags")


if __name__ == "__main__":
    main()
