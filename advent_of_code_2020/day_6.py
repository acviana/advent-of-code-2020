def load_data() -> list:
    with open("inputs/day_6_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_split_data(data) -> list:
    output = [data[0]]
    for item in data[1:]:
        if item != "":
            output[-1] = f"{output[-1]} {item}"
        else:
            output += [item]
    return output


def get_unique_answers(answers) -> set:
    output = set(answers)
    output.discard(" ")
    return output


def main():
    data = get_split_data(load_data())
    print(f"Dataset contains {len(data)} items")
    print(f"|{data[0]}|")
    unique_yes_answers_per_group = [len(get_unique_answers(item)) for item in data]
    print(unique_yes_answers_per_group)
    print(f"Total yes answers in set: {sum(unique_yes_answers_per_group)}")


if __name__ == "__main__":
    main()
