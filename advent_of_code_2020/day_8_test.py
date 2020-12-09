from advent_of_code_2020.day_8 import execute_instruction, parse_data, run_program

TEST_DATA = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

TEST_PARSED_DATA = [
    {"amount": 0, "operation": "nop", "sign": "+"},
    {"amount": 1, "operation": "acc", "sign": "+"},
    {"amount": 4, "operation": "jmp", "sign": "+"},
    {"amount": 3, "operation": "acc", "sign": "+"},
    {"amount": 3, "operation": "jmp", "sign": "-"},
    {"amount": 99, "operation": "acc", "sign": "-"},
    {"amount": 1, "operation": "acc", "sign": "+"},
    {"amount": 4, "operation": "jmp", "sign": "-"},
    {"amount": 6, "operation": "acc", "sign": "+"},
]


def test_parse_data():
    assert parse_data(TEST_DATA.split("\n")) == TEST_PARSED_DATA


def test_execute_instruction():
    assert execute_instruction(position=0, accumulator=0, **TEST_PARSED_DATA[0]) == {
        "position": 1,
        "accumulator": 0,
    }
    assert execute_instruction(position=1, accumulator=0, **TEST_PARSED_DATA[1]) == {
        "position": 2,
        "accumulator": 1,
    }
    assert execute_instruction(position=2, accumulator=1, **TEST_PARSED_DATA[2]) == {
        "position": 6,
        "accumulator": 1,
    }


def test_run_program():
    assert run_program(TEST_PARSED_DATA) == {
        "accumulator": 5,
        "termination_mode": "repeat",
    }
