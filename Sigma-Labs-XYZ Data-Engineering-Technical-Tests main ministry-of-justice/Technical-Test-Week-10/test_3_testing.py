"""Unit tests for the test_3 script"""
from test_3 import sum_current_time


def test_sum_to_six():
    """Tests to see if a valid time adds up to 6"""
    assert sum_current_time("01:02:03") == 6


def test_sum_max_time():
    """Tests to see if a valid time at max limits adds up to 141"""
    assert sum_current_time("59:59:23") == 141


def test_invalid_negative():
    """Tests to see if an invalid time using negative values, returns a 0"""
    assert sum_current_time("-01:-02:-03") == 0


def test_invalid_time():
    """Tests to see if an invalid time using values over max, returns a 0"""
    assert sum_current_time("67:60:25") == 0
