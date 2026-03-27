import pytest
from main import add, subtract, multiply, divide


@pytest.mark.parametrize("a,b,expected", [
    (2, 5, 7),
    (2, 0, 2),
    (-3.5, 2.5, -1),
    (-2, -7, -9),
])


def test_add_correct(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    (2, "5", TypeError),
])


def test_add_errors(a, b, error_type):
    with pytest.raises(error_type):
        add(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 8),
    (10.1, 5.1, 5),
    (-2, 3, -5),
])


def test_subtract_correct(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    (10, "2", TypeError),
])


def test_subtract_errors(a, b, error_type):
    with pytest.raises(error_type):
        subtract(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (0, 1, 0),
    (3, 4, 12),
    (-2, 4, -8),
])


def test_multiply_correct(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    ("1", 2, TypeError),
])


def test_multiply_errors(a, b, error_type):
    with pytest.raises(error_type):
        multiply(a, b)


@pytest.mark.parametrize('a, b, expected', [
    (6, 2, 3),
    (3, 2, 1.5),
])

def test_divide_correct(a, b, expected):
    assert divide(a, b) == expected

def test_divide_str():
    with pytest.raises(TypeError):
        divide('-10', 2)

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)