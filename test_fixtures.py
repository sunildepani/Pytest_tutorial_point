import pytest


@pytest.fixture
def input_value():
    input = 39
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


def test_divisible_by_5(input_data):
    assert input_data % 5 == 0


def test_divisible_by_10(input_data):
    assert input_data % 10 == 0

def test_divisible_by_2(input_data):
    assert input_data % 2 == 0
