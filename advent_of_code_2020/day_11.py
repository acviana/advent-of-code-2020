from collections import Counter
from typing import List
import copy


def load_data() -> List[str]:
    with open("inputs/day_11_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_data_slice(row_position, column_position, data):
    row_range_min = max(row_position - 1, 0)
    row_range_max = min(row_position + 1, len(data))
    column_range_min = max(column_position - 1, 0)
    column_range_max = min(column_position + 1, len(data))
    return[
        item[column_range_min:column_range_max + 1]
        for item in data[row_range_min:row_range_max + 1]
    ]


def get_neighbors(data_slice, central_value):
    neighbors = Counter("".join(data_slice))
    neighbors[central_value] -= 1
    return neighbors


def get_next_state(row_position, column_position, data):
    current_value = data[row_position][column_position]
    if current_value == ".":
        return "."
    data_slice = get_data_slice(row_position, column_position, data)
    neighbors = get_neighbors(data_slice, current_value)
    if current_value == "L" and neighbors["#"] == 0:
        return "#"
    elif current_value == "#" and neighbors["#"] >= 4:
        return "L"
    else:
        return current_value


def get_next_data_set(data):
    return [
        "".join(
            [
                get_next_state(row_position, column_position, data)
                for column_position in range(0, len(data[0]))
            ]
        ) for row_position in range(0, len(data))
    ]


def get_final_state(current_data):
    next_data = get_next_data_set(current_data)
    while not current_data == next_data:
        current_data = copy.deepcopy(next_data)
        next_data = get_next_data_set(current_data)
    return current_data


def count_occupied_seats(data):
    return sum([Counter(item)["#"] for item in data])


def main() -> None:
    data = load_data()
    final_state = get_final_state(data)
    occupied_seats = count_occupied_seats(final_state)
    print(f"Occupied Seats: {occupied_seats}")


if __name__ == "__main__":
    main()
