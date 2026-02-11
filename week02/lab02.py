"""Lab 02 implementations: factorial, is_prime, reverse_string

These implementations follow the provided NumPy-style docstrings
and are intended for use with GitHub Copilot during the lab.
"""

def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer to calculate the factorial of.

    Returns
    -------
    int
        The factorial of n. Returns 1 for n = 0.

    Examples
    --------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(number):
    """Check if a number is a prime number.

    A prime number is a natural number greater than 1 that has no
    positive divisors other than 1 and itself.

    Parameters
    ----------
    number : int
        The integer to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.

    Examples
    --------
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    # check odd divisors up to sqrt(number)
    import math

    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
    return True


def reverse_string(s):
    """Reverse a given string.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return s[::-1]
"""Lab 02: AI-assisted development - function implementations

Implementations for: factorial, is_prime, reverse_string
"""


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

    Examples
    --------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
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

    A prime number is a natural number greater than 1 that has no
    positive divisors other than 1 and itself.

    Parameters
    ----------
    number : int
        The integer to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.

    Examples
    --------
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    import math

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

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return s[::-1]
