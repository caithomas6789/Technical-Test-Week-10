from test_3 import sum_current_time


def test_sum_to_six():
    assert sum_current_time("01:02:03") == 6


def test_sum_max_time():
    assert sum_current_time("59:59:23") == 141


def test_invalid_negative():
    assert sum_current_time("-01:-02:-03") == 0


def test_invalid_time():
    assert sum_current_time("67:60:25") == 0
