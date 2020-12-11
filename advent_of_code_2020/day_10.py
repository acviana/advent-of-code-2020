from collections import Counter
from typing import List


def load_data() -> List[str]:
    with open("inputs/day_10_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]):
    data = [int(item) for item in data]
    data.sort()
    return [0] + data + [data[-1] + 3]


def calc_differences(parsed_data):
    return [
        parsed_data[counter + 1] - parsed_data[counter]
        for counter in range(0, len(parsed_data) - 1)
    ]


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    differences = calc_differences(parsed_data)
    count = Counter(differences)
    print(count[1] * count[3])


if __name__ == "__main__":
    main()
