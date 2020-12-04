def load_data():
    with open("inputs/day_4_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def get_split_data(data):
    output = [data[0]]
    for item in data[1:]:
        if item != "":
            output[-1] = f"{output[-1]} {item}"
        else:
            output += [item]
    return output


def tokenizer(group):
    return {item.split(":")[0]: item.split(":")[1] for item in group.strip().split(" ")}


def check_credentials(credentials):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    credentials.pop("cid", None)
    return set(credentials.keys()) == set(required_fields)


def main():
    data = load_data()
    print(f"Loaded {len(data)} rows of data")
    split_data = get_split_data(data)
    print(f"Found {len(split_data)} sets of credentials")
    tokenized_data = [tokenizer(item) for item in split_data]
    valid_credential_count = sum([check_credentials(item) for item in tokenized_data])
    print(f"Found {valid_credential_count} valid credentials")


def test_foo():
    test_result = get_split_data(load_data()[0:13])
    expected_result = [
        "byr:1983 iyr:2017 pid:796082981 cid:129 eyr:2030 ecl:oth hgt:182cm",
        " iyr:2019 cid:314 eyr:2039 hcl:#cfa07d hgt:171cm ecl:#0180ce byr:2006 pid:8204115568",
        " byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry",
        " hcl:231d64 cid:124 ecl:gmt eyr:2039 hgt:189in pid:#9c3ea1",
    ]
    assert test_result == expected_result

    test_result = [tokenizer(item) for item in expected_result]
    expected_result = [
        {
            "byr": "1983",
            "cid": "129",
            "ecl": "oth",
            "eyr": "2030",
            "hgt": "182cm",
            "iyr": "2017",
            "pid": "796082981",
        },
        {
            "byr": "2006",
            "cid": "314",
            "ecl": "#0180ce",
            "eyr": "2039",
            "hcl": "#cfa07d",
            "hgt": "171cm",
            "iyr": "2019",
            "pid": "8204115568",
        },
        {
            "byr": "1991",
            "ecl": "gry",
            "eyr": "2022",
            "hcl": "#341e13",
            "hgt": "167cm",
            "iyr": "2016",
            "pid": "729933757",
        },
        {
            "cid": "124",
            "ecl": "gmt",
            "eyr": "2039",
            "hcl": "231d64",
            "hgt": "189in",
            "pid": "#9c3ea1",
        },
    ]
    assert test_result == expected_result

    test_result = [check_credentials(item) for item in expected_result]
    expected_result = [False, True, True, False]
    assert test_result == expected_result


if __name__ == "__main__":
    test_foo()
    main()
