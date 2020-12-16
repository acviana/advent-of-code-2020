from collections import Counter
from typing import List
import copy


def load_data() -> List[str]:
    with open("inputs/day_11_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_nearest_neighbors_slice(
    row_position: int, column_position: int, data: List[str]
) -> List[str]:
    row_range_min = max(row_position - 1, 0)
    row_range_max = min(row_position + 1, len(data))
    column_range_min = max(column_position - 1, 0)
    column_range_max = min(column_position + 1, len(data))
    return [
        item[column_range_min : column_range_max + 1]
        for item in data[row_range_min : row_range_max + 1]
    ]


def get_line_of_sight(
    row_start_position: int,
    column_start_position: int,
    delta_row: int,
    delta_column: int,
    data: List[str],
) -> str:
    step = 1
    next_position = ""
    # Forgive me, it's late.
    while 1 == 1:
        row_position = row_start_position + (step * delta_row)
        if row_position > len(data) - 1 or row_position < 0:
            return next_position
        column_position = column_start_position + (step * delta_column)
        if column_position > len(data[0]) - 1 or column_position < 0:
            return next_position
        next_position = data[row_position][column_position]
        if next_position in ["#", "L"]:
            return next_position
        else:
            step += 1
    assert False


def get_line_of_sight_neighbors_slice(
    row_position: int, column_position: int, data: List[str]
) -> List[str]:
    output = []
    for delta_row in range(-1, 2):
        for delta_column in range(-1, 2):
            if not delta_row == 0 or not delta_column == 0:
                line_of_sight = get_line_of_sight(
                    row_position, column_position, delta_row, delta_column, data
                )
                if line_of_sight != "":
                    output += [line_of_sight]
    output += [data[row_position][column_position]]
    return output


def get_data_slice(
    row_position: int, column_position: int, data: List[str], mode: str
) -> List[str]:
    if mode == "nearest_neighbors":
        return get_nearest_neighbors_slice(row_position, column_position, data)
    elif mode == "line_of_sight":
        return get_line_of_sight_neighbors_slice(row_position, column_position, data)
    else:
        assert False


def get_neighbors(data_slice: List[str], central_value: str):
    neighbors = Counter("".join(data_slice))
    neighbors[central_value] -= 1
    return neighbors


def get_next_state(
    row_position: int, column_position: int, data: List[str], mode: str
) -> str:
    if mode == "nearest_neighbors":
        tolerance = 4
    elif mode == "line_of_sight":
        tolerance = 5
    else:
        assert False
    current_value = data[row_position][column_position]
    if current_value == ".":
        return "."
    data_slice = get_data_slice(row_position, column_position, data, mode)
    neighbors = get_neighbors(data_slice, current_value)
    if current_value == "L" and neighbors["#"] == 0:
        return "#"
    elif current_value == "#" and neighbors["#"] >= tolerance:
        return "L"
    else:
        return current_value


def get_next_data_set(data: List[str], mode: str) -> List[str]:
    return [
        "".join(
            [
                get_next_state(row_position, column_position, data, mode)
                for column_position in range(0, len(data[0]))
            ]
        )
        for row_position in range(0, len(data))
    ]


def get_final_state(current_data: List[str], mode: str) -> List[str]:
    next_data = get_next_data_set(current_data, mode)
    while not current_data == next_data:
        current_data = copy.deepcopy(next_data)
        next_data = get_next_data_set(current_data, mode)
    return current_data


def count_occupied_seats(data: List[str]) -> int:
    return sum([Counter(item)["#"] for item in data])


def main() -> None:
    data = load_data()
    final_state = get_final_state(data, mode="nearest_neighbors")
    occupied_seats = count_occupied_seats(final_state)
    print(f"Occupied Seats: {occupied_seats}")

    final_state = get_final_state(data, mode="line_of_sight")
    occupied_seats = count_occupied_seats(final_state)
    print(f"Occupied Seats: {occupied_seats}")


if __name__ == "__main__":
    main()
