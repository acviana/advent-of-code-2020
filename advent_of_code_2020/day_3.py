from collections import Counter
import math


def load_data():
    with open("inputs/day_3_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_column_multiplier(row_size, column_size, row_step_size, column_step_size):
    steps_to_bottom = row_size / row_step_size
    minimum_columns = steps_to_bottom * column_step_size
    column_multiplier = math.ceil(minimum_columns / column_size)
    return column_multiplier


def get_expanded_data(data, column_multiplier):
    return [row * column_multiplier for row in data]


def get_path_values(data, row_step_size, column_step_size):
    row_position = 0
    column_position = 0
    path_values = []

    while row_position != len(data):
        path_values += data[row_position][column_position]
        row_position += row_step_size
        column_position += column_step_size

    return path_values


def main():
	# Expand the data to fit the required path
    row_step_size = 1
    column_step_size = 3
    print(f"Step Size is {row_step_size} rows x {column_step_size} columns")
    original_data = load_data()
    print(
        f"Original Data is {len(original_data)} rows x {len(original_data[0])} columns"
    )
    column_multiplier = get_column_multiplier(
        row_size=len(original_data),
        column_size=len(original_data[0]),
        row_step_size=1,
        column_step_size=3,
    )
    print(f"Column Multiplier is {column_multiplier}")
    data = get_expanded_data(data=original_data, column_multiplier=column_multiplier)
    print(f"Expanded data is {len(data)} rows x {len(data[0])} columns")

    # Walk the path and count the trees
    path_values = get_path_values(
        data=data, row_step_size=row_step_size, column_step_size=column_step_size
    )
    print(f"Path is {len(path_values)} long")
    tree_count = Counter(path_values)["#"]
    print(f"{tree_count} trees in path")


if __name__ == "__main__":
    assert get_column_multiplier(100, 10, 1, 3) == 30
    assert get_column_multiplier(100, 7, 1, 3) == 43
    main()
