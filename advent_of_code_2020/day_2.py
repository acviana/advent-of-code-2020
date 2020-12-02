from collections import Counter


def load_data():
    with open("inputs/day_2_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def tokenize_data(row):
    rule, data = row.split(":")
    limits, letter = rule.split(" ")
    lower_limit, upper_limit = limits.split("-")
    return {
        "data": data.strip(),
        "letter": letter,
        "lower_limit": int(lower_limit),
        "upper_limit": int(upper_limit),
    }


def check_password_a(tokenized_data):
    letter_count = Counter(tokenized_data["data"])[tokenized_data["letter"]]
    if letter_count < tokenized_data["lower_limit"]:
        return False
    elif letter_count > tokenized_data["upper_limit"]:
        return False
    else:
        return True


def check_password_b(tokenized_data):
    position_1_check = (
        tokenized_data["data"][tokenized_data["lower_limit"] - 1]
        == tokenized_data["letter"]
    )
    position_2_check = (
        tokenized_data["data"][tokenized_data["upper_limit"] - 1]
        == tokenized_data["letter"]
    )
    if position_1_check != position_2_check:
        return True
    else:
        return False


def main():
    data = load_data()
    valid_password_count = sum([check_password_a(tokenize_data(item)) for item in data])
    print(f'{valid_password_count} valid "a" form passwords out of {len(data)}')

    valid_password_count = sum([check_password_b(tokenize_data(item)) for item in data])
    print(f'{valid_password_count} valid "b" form passwords out of {len(data)}')


if __name__ == "__main__":
    main()
