import math


def load_data():
    with open("inputs/day_5_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def binary_partition(instruction, bottom, top):
    if instruction in ["F", "L"]:
        return {"top": top - math.ceil((top - bottom) / 2), "bottom": bottom}
    elif instruction in ["B", "R"]:
        return {"top": top, "bottom": bottom + math.ceil((top - bottom) / 2)}


def parse_seat_instrcutions(instructions, size):
    position = {"bottom": 0, "top": size - 1}
    for instruction in instructions:
        position = binary_partition(instruction, **position)
    return position


def get_seat_id(instructions):
    row = parse_seat_instrcutions(instructions[:8], 128)["top"]
    column = parse_seat_instrcutions(instructions[7:], 8)["top"]
    return row * 8 + column


def main():
    data = load_data()
    seats = [get_seat_id(item) for item in data]
    print(f"Largest Seat ID: {max(seats)}")
    print(f"Empty Seats: {set(range(0, 128 * 8)) - set(seats)}")


if __name__ == "__main__":
    main()
