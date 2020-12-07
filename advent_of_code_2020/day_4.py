from typing import Dict, List


def load_data() -> List[str]:
    with open("inputs/day_4_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def get_split_data(data: List[str]) -> List[str]:
    output = [data[0]]
    for item in data[1:]:
        if item != "":
            output[-1] = f"{output[-1]} {item}"
        else:
            output += [item]
    return output


def tokenizer(group: str) -> Dict[str, str]:
    return {item.split(":")[0]: item.split(":")[1] for item in group.strip().split(" ")}


def check_credential_fields(credentials: Dict[str, str]) -> bool:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    credentials.pop("cid", None)
    return True if (set(credentials.keys()) == set(required_fields)) else False


def check_year(year: int, lower_limit: int, upper_limit: int) -> bool:
    return True if year >= lower_limit and year <= upper_limit else False


def parse_height(height: str):
    return {
        "units": height[-2:],
        "measurement": int(height[:-2]),
    }


def check_height(units: str, measurement: int) -> bool:
    if units == "cm":
        return True if measurement >= 150 and measurement <= 193 else False
    if units == "in":
        return True if measurement >= 59 and measurement <= 76 else False
    else:
        assert False


def check_hair_color(hair_color: str) -> bool:
    # I refuse to do this regex
    if hair_color[0] != "#":
        return False
    allowed_characters = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    for character in hair_color[1:]:
        if character not in allowed_characters:
            return False
    return True


def check_eye_color(eye_color: str) -> bool:
    allowed_values = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    return True if eye_color in allowed_values else False


def check_passport_id(passport_id: str) -> bool:
    if not passport_id.isdigit():
        return False
    return True if len(passport_id) == 9 else False


def check_credentials(credentials: Dict[str, str]) -> bool:
    if not check_credential_fields(credentials):
        return False
    if not check_year(int(credentials["byr"]), 1920, 2002):
        return False
    if not check_year(int(credentials["iyr"]), 2010, 2020):
        return False
    if not check_year(int(credentials["eyr"]), 2020, 2030):
        return False
    if credentials["hgt"].isalpha():
        return False
    if not check_height(**parse_height(credentials["hgt"])):
        return False
    if not check_hair_color(credentials["hcl"]):
        return False
    if not check_eye_color(credentials["ecl"]):
        return False
    if not check_passport_id(credentials["pid"]):
        return False
    return True


def main(data: List[str]) -> None:
    print(f"Loaded {len(data)} rows of data")
    split_data = get_split_data(data)
    print(f"Found {len(split_data)} sets of credentials")
    tokenized_data = [tokenizer(item) for item in split_data]
    valid_credentials = [check_credentials(item) for item in tokenized_data]
    valid_credential_count = sum(valid_credentials)
    print(f"Found {valid_credential_count} valid credentials")


if __name__ == "__main__":
    main(data=load_data())
