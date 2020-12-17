from typing import Dict, List


def load_data() -> List[str]:
    with open("inputs/day_12_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]) -> List[Dict]:
    return [{"direction": item[0], "magnitude": int(item[1:])} for item in data]


def apply_instruction(
    x_position: int, y_position: int, direction: str, magnitude: int, orientation: int
) -> Dict[str, int]:
    if direction == "N":
        return {
            "x_position": x_position,
            "y_position": y_position + magnitude,
            "orientation": orientation,
        }
    elif direction == "S":
        return {
            "x_position": x_position,
            "y_position": y_position - magnitude,
            "orientation": orientation,
        }
    elif direction == "E":
        return {
            "x_position": x_position + magnitude,
            "y_position": y_position,
            "orientation": orientation,
        }
    elif direction == "W":
        return {
            "x_position": x_position - magnitude,
            "y_position": y_position,
            "orientation": orientation,
        }
    elif direction == "L":
        return {
            "x_position": x_position,
            "y_position": y_position,
            "orientation": (orientation + magnitude) % 360,
        }
    elif direction == "R":
        return {
            "x_position": x_position,
            "y_position": y_position,
            "orientation": (orientation - magnitude) % 360,
        }
    elif direction == "F":
        if orientation == 0:
            direction = "E"
        elif orientation == 90:
            direction = "N"
        elif orientation == 180:
            direction = "W"
        elif orientation == 270:
            direction = "S"
        else:
            assert False
        return apply_instruction(
            x_position, y_position, direction, magnitude, orientation
        )
    else:
        assert False


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)

    current_location = {
        "x_position": 0,
        "y_position": 0,
        "orientation": 0,
    }
    for instruction in parsed_data:
        current_location = apply_instruction(**current_location, **instruction)

    print(current_location)
    print(
        f"Manhatten Distance is: "
        f"{abs(current_location['x_position']) + abs(current_location['y_position'])}"
    )


if __name__ == "__main__":
    main()
