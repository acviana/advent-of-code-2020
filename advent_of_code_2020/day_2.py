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


def check_password_a(data, letter, lower_limit, upper_limit):
    letter_count = Counter(data)[letter]
    if letter_count < lower_limit:
        return False
    elif letter_count > upper_limit:
        return False
    else:
        return True


def check_password_b(data, letter, lower_limit, upper_limit):
    position_1_check = data[lower_limit - 1] == letter
    position_2_check = data[upper_limit - 1] == letter
    if position_1_check != position_2_check:
        return True
    else:
        return False


def main():
    data = load_data()
    valid_password_count = sum(
        [check_password_a(**tokenize_data(item)) for item in data]
    )
    print(f'{valid_password_count} valid "a" form passwords out of {len(data)}')

    valid_password_count = sum(
        [check_password_b(**tokenize_data(item)) for item in data]
    )
    print(f'{valid_password_count} valid "b" form passwords out of {len(data)}')


if __name__ == "__main__":
    main()
