from advent_of_code_2020.day_6 import get_unique_answers


def test_get_unique_answers():
    # , ' ovuxdgiheszjbaltw oxwjiubhfylzavst', ' se u j se'
    assert get_unique_answers('b b b b') == {"b"}
    assert get_unique_answers(' x xfkj xb') == {"b"}
