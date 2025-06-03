import pytest
from ops import *

def test_add() -> None:
    """Tests the add function."""
    assert add(2,3) == 5

def test_subtract() -> None:
    """Tests the subtract function."""
    assert subtract(2, 3) == -1

def test_multiply() -> None:
    """Tests the multiply function."""
    assert multiply(2, 3) == 6

def test_divide() -> None:
    """Tests the divide function."""
    assert divide(10,5) == 2

def test_divide_by_zero() -> None:
    """Tests the divide function for division by zero."""
    with pytest.raises(ValueError):
        divide(10, 0)