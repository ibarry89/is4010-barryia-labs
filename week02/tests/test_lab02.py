import os
import sys

# Ensure week02 is importable when running tests from repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import lab02 as L


def test_factorial_basic():
    assert L.factorial(5) == 120
    assert L.factorial(0) == 1


def test_factorial_errors():
    with pytest.raises(TypeError):
        L.factorial(2.5)
    with pytest.raises(ValueError):
        L.factorial(-1)


def test_is_prime_basic():
    assert L.is_prime(2)
    assert L.is_prime(17)
    assert not L.is_prime(1)
    assert not L.is_prime(4)
    assert not L.is_prime(0)


def test_is_prime_nonint():
    with pytest.raises(TypeError):
        L.is_prime(3.14)


def test_reverse_string_basic():
    assert L.reverse_string("hello") == "olleh"
    assert L.reverse_string("") == ""


def test_reverse_string_typeerror():
    with pytest.raises(TypeError):
        L.reverse_string(123)
