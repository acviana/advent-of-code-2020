from typing import List


def load_data() -> List[str]:
    with open("inputs/day_6_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_split_data(data: List[str]) -> List[str]:
    output = [data[0]]
    for item in data[1:]:
        if item != "":
            output[-1] = f"{output[-1]} {item}"
        else:
            output += [item]
    return output


def get_unique_answers(answers: str) -> set:
    output = set(answers)
    output.discard(" ")
    return output


def get_unanimous_answers(answers: str) -> set:
    return set.intersection(*[set(item) for item in answers.split()])


def main() -> None:
    data = get_split_data(load_data())
    print(f"Dataset contains {len(data)} items")
    unique_yes_answers_per_group = [len(get_unique_answers(item)) for item in data]
    print(f"Total yes answers in set: {sum(unique_yes_answers_per_group)}")

    get_unanimous_answers_per_group = [
        len(get_unanimous_answers(item)) for item in data
    ]
    print(f"Total unanimous answers in set: {sum(get_unanimous_answers_per_group)}")


if __name__ == "__main__":
    main()
