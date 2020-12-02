from itertools import combinations
from math import prod


def load_data():
    with open("advent_of_code_2020/input_1.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]


def match_by_sum_and_multiply(input_list, set_size, match_sum):
    for combination in combinations(input_list, set_size):
        if sum(combination) == match_sum:
            return combination


def main():
    data = load_data()

    combination = match_by_sum_and_multiply(data, 2, 2020)
    print(
        f"Set: {*combination,}, Sum: {sum(combination)}, Product: {prod(combination)}"
    )

    combination = match_by_sum_and_multiply(data, 3, 2020)
    print(
        f"Set: {*combination,}, Sum: {sum(combination)}, Product: {prod(combination)}"
    )


if __name__ == "__main__":
    main()
