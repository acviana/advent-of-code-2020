from collections import Counter, defaultdict
from math import prod
from typing import DefaultDict, Dict, List


def load_data() -> List[str]:
    with open("inputs/day_10_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]) -> List[int]:
    output = [int(item) for item in data]
    output.sort()
    return [0] + output + [output[-1] + 3]


def calc_differences(parsed_data: List[int]) -> List[int]:
    return [
        parsed_data[counter + 1] - parsed_data[counter]
        for counter in range(0, len(parsed_data) - 1)
    ]


def get_node_mappings(parsed_data: List[int]) -> Dict[int, List[int]]:
    node_mappings = {
        number: [item for item in range(number + 1, number + 4) if item in parsed_data]
        for number in parsed_data
    }
    node_mappings[parsed_data[-1]] = [parsed_data[-1]]
    return node_mappings


def calc_step(current_data: DefaultDict[int, int], node_mappings: Dict[int, List[int]]):
    new_data: DefaultDict[int, int] = defaultdict(int)
    for node in current_data:
        for next_node in node_mappings[node]:
            new_data[next_node] += current_data[node]
    return new_data


def calc_all_paths(parsed_data: List[int]) -> int:
    node_mappings = get_node_mappings(parsed_data)
    current_data = defaultdict(int)
    current_data[0] = 1
    while not list(current_data.keys()) == [parsed_data[-1]]:
        current_data = calc_step(current_data, node_mappings)
    return current_data[parsed_data[-1]]


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    differences = calc_differences(parsed_data)
    print(prod(differences))
    count = Counter(differences)
    print(count[1] * count[3])

    possible_paths = calc_all_paths(parsed_data)
    print(f"Total possible paths: {possible_paths}")


if __name__ == "__main__":
    main()
