# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
```
Context: I have a simple Python function that is intended to sum
all even numbers in a list, but it's producing incorrect results.

Persona: You are a senior Python developer skilled at debugging.

Task: Identify the logical error and provide a corrected implementation.

Format: Return the corrected function in a Python code block and a one-line
explanation of the bug.

Code:
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
```

**What I Learned:**
- The wrong parity check (`% 2 == 1`) summed odd numbers instead of even.

---

## Problem 2: Refactoring

**My Prompt:**
```
Context: The function below returns names of users who are 18 or older.
It's correct but not very Pythonic or readable.

Persona: You are a senior Python developer who loves idiomatic code.

Task: Refactor the function to be more concise, Pythonic, and readable.

Format: Provide the refactored function in a Python code block and a short
note explaining the improvements.

Code:
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    """Return names of users aged 18 or older.

    Parameters
    ----------
    users : list of dict
        Each dict must contain 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user.get('age', 0) >= 18]
```

**What I Learned:**
- List comprehensions make this operation clearer and avoid index-based access.

---

## Problem 3: Documenting

**My Prompt:**
```
Context: I have a function that calculates area but it lacks documentation.

Persona: You are a technical writer and senior Python developer.

Task: Write a NumPy-style docstring for the function, mentioning that it
raises ValueError when inputs are non-positive.

Format: Provide the full function with the NumPy-style docstring in a
Python code block.

Code:
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be positive.
    width : float
        The width of the rectangle. Must be positive.

    Returns
    -------
    float
        The area computed as `length * width`.

    Raises
    ------
    ValueError
        If `length` or `width` is not a positive number.

    Examples
    --------
    >>> calculate_area(2, 3)
    6
    >>> calculate_area(0.5, 4)
    2.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
- Explicitly documenting parameter types, return values, and raised exceptions
  helps both humans and AI tools to reason about code.
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt (CPTF):**
```
Context: I have this Python function that should return the sum of all even numbers in a list. It currently returns the wrong total.

Persona: You are a senior Python developer and code reviewer.

Task: Identify the logical bug and provide the corrected implementation. Explain what was wrong in one sentence.

Format: Provide the corrected function in a Python code block and a one-sentence explanation.

Code:
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
```

**What I Learned:**
- The conditional was inverted; checking `num % 2 == 0` selects even numbers.

---

## Problem 2: Refactoring

**My Prompt (CPTF):**
```
Context: This function works but is written in a non-Pythonic style using index-based loops.

Persona: You are a senior Python developer who prefers readable, idiomatic code.

Task: Refactor the function to be concise, clearer, and Pythonic (use meaningful names and list comprehensions where appropriate).

Format: Provide the refactored function in a Python code block and a one-line rationale.

Code:
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    """Return names of users aged 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user.get('age', 0) >= 18]
```

**What I Learned:**
- List comprehensions make the code shorter and clearer; `user.get('age', 0)` is safer for missing keys.

---

## Problem 3: Documenting

**My Prompt (CPTF):**
```
Context: This function calculates the area of a rectangle and raises for invalid inputs.

Persona: You are a technical writer and senior Python developer who writes NumPy-style docstrings.

Task: Produce a NumPy-style docstring describing parameters, return value, and the ValueError raised for non-positive inputs.

Format: Provide only the function with the new docstring in a Python code block.

Code:
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be a positive number.
    width : float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The area of the rectangle (length * width).

    Raises
    ------
    ValueError
        If either `length` or `width` is not a positive number.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
- Explicit NumPy-style sections (`Parameters`, `Returns`, `Raises`) make the function contract clear to humans and AI tools.
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
```
You are a senior Python developer. I have a function that's supposed to sum 
all even numbers in a list, but it's giving wrong results. Here's the code:

def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total

For example, sum_of_evens([2, 4, 5, 6]) should return 12 (2+4+6), but 
it's returning the wrong value. Can you identify the logical error and 
provide the corrected code in a Python code block?
```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: Changed from == 1 to == 0
            total += num
    return total
```

**What I Learned:**
The bug was in the conditional check. The original code checked `if num % 2 == 1`, which checks for odd numbers. For even numbers, we need `if num % 2 == 0`. This is a common off-by-one logic error that can be hard to spot without testing the code.

---

## Problem 2: Refactoring

**My Prompt:**
```
You are a senior Python developer helping a junior developer improve their code. 
This function works correctly, but it's not very Pythonic or readable:

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

Please refactor this to be more Pythonic and readable. Use modern Python patterns 
like list comprehensions or built-in functions. Provide the improved code in a 
Python code block with a brief explanation of what makes it more Pythonic.
```

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**
The refactored version uses a list comprehension instead of a for loop with append(). This is more Pythonic because it's more concise, readable, and efficient. Also, the original code used `range(len(users))` with index access, which is an anti-pattern in Python. The improved version directly iterates over the users, which is clearer and more Pythonic.

---

## Problem 3: Documenting

**My Prompt:**
```
You are a senior Python developer. I have a function that works correctly 
but has no documentation:

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

Please write a professional NumPy-style docstring for this function. 
Make sure to include sections for Parameters, Returns, Raises, and Examples. 
Format it as a Python code block.
```

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle given its dimensions.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be a positive number.
    width : float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The area of the rectangle (length × width).

    Raises
    ------
    ValueError
        If length or width is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(5, 3)
    15
    >>> calculate_area(2.5, 4)
    10.0
    >>> calculate_area(-2, 5)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
A good NumPy-style docstring clearly communicates the purpose of a function, what it expects as input, what it returns, and any exceptions it might raise. The Examples section is particularly important because it shows users exactly how to use the function. This documentation also helps AI tools like GitHub Copilot understand what the function should do when generating code.
