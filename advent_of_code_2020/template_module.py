from typing import List


def load_data() -> List[str]:
    with open("inputs/day_X_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]):
    pass


def main() -> None:
    data = load_data()
    parse_data(data)


if __name__ == "__main__":
    main()
