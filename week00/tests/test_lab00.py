# test_lab00.py
# Setup verification tests - intentionally simple

from lab00 import hello_world, add_numbers


def test_hello_world():
    """Test that hello_world returns the expected greeting."""
    result = hello_world()
    assert result == "Hello, IS4010!"
    assert isinstance(result, str)


def test_add_numbers():
    """Test that add_numbers correctly adds two numbers."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, 20) == 30
    assert add_numbers(1.5, 2.5) == 4.0
