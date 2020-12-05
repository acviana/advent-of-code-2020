from advent_of_code_2020.day_4 import (
    check_year,
    check_height,
    check_hair_color,
    check_eye_color,
    check_credentials,
    check_credential_fields,
    get_split_data,
    load_data,
    tokenizer,
)


def test_get_split_data():
    test_result = get_split_data(load_data()[0:13])
    expected_result = [
        "byr:1983 iyr:2017 pid:796082981 cid:129 eyr:2030 ecl:oth hgt:182cm",
        " iyr:2019 cid:314 eyr:2039 hcl:#cfa07d hgt:171cm ecl:#0180ce byr:2006 pid:8204115568",
        " byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry",
        " hcl:231d64 cid:124 ecl:gmt eyr:2039 hgt:189in pid:#9c3ea1",
    ]
    assert test_result == expected_result


def test_tokenizer():
    test_input = [
        "byr:1983 iyr:2017 pid:796082981 cid:129 eyr:2030 ecl:oth hgt:182cm",
        " iyr:2019 cid:314 eyr:2039 hcl:#cfa07d hgt:171cm ecl:#0180ce byr:2006 pid:8204115568",
        " byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry",
        " hcl:231d64 cid:124 ecl:gmt eyr:2039 hgt:189in pid:#9c3ea1",
    ]
    test_result = [tokenizer(item) for item in test_input]
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


def test_check_credential_fields():
    test_input = [
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
    test_result = [check_credential_fields(item) for item in test_input]
    expected_result = [False, True, True, False]
    assert test_result == expected_result


def test_check_year():
    assert check_year("1920", 1920, 2002)
    assert check_year("1974", 1920, 2002)
    assert check_year("1921", 1920, 2002)
    assert check_year("2002", 1920, 2002)
    # assert not check_year("aa", 1920, 2002)


def test_check_height():
    assert not check_height("149cm")
    assert check_height("150cm")
    assert check_height("151cm")
    assert check_height("192cm")
    assert check_height("193cm")
    assert not check_height("194cm")

    assert check_height("60in")
    assert check_height("190cm")
    assert not check_height("190in")
    assert not check_height("190")


def test_check_hair_color():
    assert check_hair_color("#123abc")
    assert not check_hair_color("#123abz")
    assert not check_hair_color("123abc")


def test_check_eye_color():
    assert check_eye_color("brn")
    assert not check_eye_color("wat")


def test_failing_credentials():
    assert not check_credentials(
        tokenizer(
            "eyr:1972 cid:100 "
            "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"
        )
    )

    assert not check_credentials(
        tokenizer(
            "iyr:2019 "
            "hcl:#602927 eyr:1967 hgt:170cm "
            "ecl:grn pid:012533040 byr:1946 "
        )
    )

    assert not check_credentials(
        tokenizer(
            "hcl:dab227 iyr:2012 "
            "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"
        )
    )

    assert not check_credentials(
        tokenizer(
            "hgt:59cm ecl:zzz "
            "eyr:2038 hcl:74454a iyr:2023 "
            "pid:3556412378 byr:2007"
        )
    )


def test_passing_credentials():
    assert check_credentials(
        tokenizer(
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 " "hcl:#623a2f"
        )
    )

    assert check_credentials(
        tokenizer(
            "eyr:2029 ecl:blu cid:129 byr:1989 "
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"
        )
    )

    assert check_credentials(
        tokenizer(
            "hcl:#888785 "
            "hgt:164cm byr:2001 iyr:2015 cid:88 "
            "pid:545766238 ecl:hzl "
            "eyr:2022"
        )
    )

    assert check_credentials(
        tokenizer(
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
        )
    )


if __name__ == "__main__":
    test_get_split_data()
    test_tokenizer()
    test_check_credential_fields()
    test_check_year()
    test_check_height()
    test_check_hair_color()
    test_failing_credentials()
    test_passing_credentials()
