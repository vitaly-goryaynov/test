import pytest


from src.practice_1.calculator import Calculator


@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [(1, 1, 2)])

def test_add_positive(value_left, value_right, expend_result):

    assert Calculator.add(value_left, value_right) == expend_result
