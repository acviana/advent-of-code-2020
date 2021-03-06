from advent_of_code_2020.day_1 import match_by_sum_and_multiply


def test_match_by_sum_and_multiply():
    test_data = [1721, 979, 366, 299, 675, 1456]
    test_result = match_by_sum_and_multiply(test_data, 2, 2020)
    assert test_result == (1721, 299)
