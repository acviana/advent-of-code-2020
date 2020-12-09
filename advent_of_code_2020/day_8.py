from typing import Dict, List
import copy


def load_data() -> List[str]:
    with open("inputs/day_8_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]) -> List[Dict]:
    return [parse_instruction(item) for item in data]


def parse_instruction(instruction: str) -> Dict:
    operation, argument = instruction.split()
    return {"operation": operation, "sign": argument[0], "amount": int(argument[1:])}


def execute_instruction(
    position: int, accumulator: int, operation: str, amount: int, sign: str
) -> Dict:
    if operation == "acc":
        return {
            "position": position + 1,
            "accumulator": (accumulator + amount)
            if sign == "+"
            else (accumulator - amount),
        }
    elif operation == "jmp":
        return {
            "position": (position + amount) if sign == "+" else (position - amount),
            "accumulator": accumulator,
        }
    elif operation == "nop":
        return {"position": position + 1, "accumulator": accumulator}
    else:
        assert False


def run_program(instructions: List[Dict]) -> Dict:
    previous_positions = set()
    position = 0
    accumulator = 0
    while position not in previous_positions:
        previous_positions.add(position)
        response = execute_instruction(
            position=position, accumulator=accumulator, **instructions[position]
        )
        if response["position"] >= len(instructions):
            return {"accumulator": response["accumulator"], "termination_mode": "exit"}
        position = response["position"]
        accumulator = response["accumulator"]
    return {"accumulator": accumulator, "termination_mode": "repeat"}


def run_altered_program(parsed_data: List[Dict]) -> Dict:
    for position, instruction in enumerate(parsed_data):
        if instruction["operation"] == "acc":
            continue
        altered_parsed_data = copy.deepcopy(parsed_data)
        altered_parsed_data[position]["operation"] = (
            "nop" if altered_parsed_data[position]["operation"] == "jmp" else "jmp"
        )
        response = run_program(altered_parsed_data)
        if response["termination_mode"] == "exit":
            return response
    assert False


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    response = run_program(parsed_data)
    print(
        f"Original program exited with status {response['termination_mode']} "
        f"and accumulator value {response['accumulator']}"
    )

    response = run_altered_program(parsed_data)
    print(
        f"Altered program exited with status {response['termination_mode']} "
        f"and accumulator value {response['accumulator']}"
    )


if __name__ == "__main__":
    main()
