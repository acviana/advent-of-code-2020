from itertools import combinations
from math import prod
from typing import List, Tuple


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]


def match_by_sum_and_multiply(
    input_list: List[int], set_size: int, match_sum: int
) -> Tuple:
    for combination in combinations(input_list, set_size):
        if sum(combination) == match_sum:
            return combination
    return ()


def summerize_result(combination: Tuple) -> str:
    return (
        f"Set: {*combination,}, Sum: {sum(combination)}, Product: {prod(combination)}"
    )


def main() -> None:
    data = load_data()

    combination = match_by_sum_and_multiply(data, 2, 2020)
    print(summerize_result(combination))

    combination = match_by_sum_and_multiply(data, 3, 2020)
    print(summerize_result(combination))


if __name__ == "__main__":
    main()
