from typing import Dict, List


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


def run_program(instructions):
    previous_positions = set()
    position = 0
    accumulator = 0
    while position not in previous_positions:
        previous_positions.add(position)
        try:
            response = execute_instruction(
                position=position, accumulator=accumulator, **instructions[position]
            )
        except IndexError:
            return {"accumulator": accumulator, "termination_mode": "exit"}
        position = response["position"]
        accumulator = response["accumulator"]
    return {"accumulator": accumulator, "termination_mode": "repeat"}


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    accumulator = run_program(parsed_data)
    print(accumulator)


if __name__ == "__main__":
    main()
