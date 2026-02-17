"""Lab 02: AI-assisted development - function implementations

Implementations for: factorial, is_prime, reverse_string
"""

from __future__ import annotations

import math


def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer to calculate the factorial of.

    Returns
    -------
    int
        The factorial of n. Returns 1 for n = 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(number: int) -> bool:
    """Check if a number is a prime number.

    Parameters
    ----------
    number : int
        The integer to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
    return True


def reverse_string(s: str) -> str:
    """Reverse a given string.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return s[::-1]
