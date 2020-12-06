from advent_of_code_2020.day_6 import (
    get_unique_answers,
    get_unanimous_answers,
)


def test_get_unique_answers():
    # , ' ovuxdgiheszjbaltw oxwjiubhfylzavst', ' se u j se'
    assert get_unique_answers("b b b b") == {"b"}
    assert get_unique_answers(" x xfkj xb") == {"x", "f", "k", "b", "j"}


def test_get_unanimous_answers():
    assert get_unanimous_answers("b b b b") == {"b"}
    assert get_unanimous_answers(" x xfkj xb") == {"x"}
