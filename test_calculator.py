import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),
        (5, -2, 3),
        (-3, -7, -10),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(calc, a, b, expected):
    result = calc.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (-9, 3, -3.0),
        (0, 5, 0.0),
        (7.5, 2.5, 3.0),
    ],
)
def test_divide(calc, a, b, expected):
    result = calc.divide(a, b)
    assert result == expected


def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (9, False),
        (15, False),
        (1, False),
        (0, False),
        (-7, False),
    ],
)
def test_is_prime_number(calc, n, expected):
    result = calc.is_prime_number(n)
    assert result == expected