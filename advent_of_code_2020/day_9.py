from itertools import combinations
from typing import List


def load_data() -> List[int]:
    with open("inputs/day_9_input.txt") as f:
        return [int(item.strip()) for item in f.readlines()]


def check_valid_number(preamble: List[int], check_value: int) -> bool:
    possible_combinations = combinations(preamble, 2)
    possible_sums = [sum(item) for item in possible_combinations]
    return True if check_value in set(possible_sums) else False


def find_invalid_number(number_list: List[int], preamble_size: int) -> int:
    for position in range(0, len(number_list) - preamble_size):
        preamble = number_list[position : position + preamble_size]
        check_value = number_list[position + preamble_size]
        result = check_valid_number(preamble=preamble, check_value=check_value)
        if not result:
            return check_value


def main() -> None:
    data = load_data()
    result = find_invalid_number(data, 25)
    print(f"First number to fail check is: {result}")


if __name__ == "__main__":
    main()
