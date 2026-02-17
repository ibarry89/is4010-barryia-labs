"""
Lab 05: Functions and Error Handling

This module demonstrates refactoring procedural code into clean, reusable functions
with robust error handling for edge cases.
"""

# Data: List of user dictionaries
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.

    This function computes the average age from a list of user dictionaries,
    skipping users with invalid or non-integer age values. It handles edge cases
    such as empty lists and missing 'age' keys gracefully.

    Parameters
    ----------
    users : list
        A list of dictionaries representing users. Each dictionary should contain
        at least an 'age' key with an integer value.

    Returns
    -------
    float
        The average age of users with valid integer ages, rounded to 2 decimal places.
        Returns 0.0 if the list is empty or contains no users with valid ages.

    Examples
    --------
    >>> users = [
    ...     {"name": "alice", "age": 30},
    ...     {"name": "bob", "age": 25},
    ...     {"name": "charlie", "age": 35}
    ... ]
    >>> calculate_average_age(users)
    30.0

    >>> calculate_average_age([])
    0.0
    """
    try:
        # Handle empty list
        if not users:
            return 0.0

        total_age = 0
        user_count_for_age = 0

        # Calculate total age of users with valid integer ages
        for user in users:
            try:
                age = user.get("age")
                if isinstance(age, int):
                    total_age += age
                    user_count_for_age += 1
            except (KeyError, TypeError):
                # Skip users with invalid age data
                continue

        # Calculate average, handling division by zero
        if user_count_for_age == 0:
            return 0.0

        return total_age / user_count_for_age

    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0
    except Exception as e:
        print(f"error: unexpected error calculating average age: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Extract email addresses from active users.

    This function retrieves email addresses from users who are marked as active.
    It handles edge cases such as empty lists, missing 'is_active' keys, and
    missing 'email' keys gracefully.

    Parameters
    ----------
    users : list
        A list of dictionaries representing users. Each dictionary should contain
        'is_active' and 'email' keys where applicable.

    Returns
    -------
    list
        A list of email addresses from active users. Returns an empty list if
        no active users have email addresses or if the input list is empty.

    Examples
    --------
    >>> users = [
    ...     {"name": "alice", "is_active": True, "email": "alice@example.com"},
    ...     {"name": "bob", "is_active": False, "email": "bob@example.com"},
    ...     {"name": "charlie", "is_active": True, "email": "charlie@example.com"}
    ... ]
    >>> sorted(get_active_user_emails(users))
    ['alice@example.com', 'charlie@example.com']

    >>> get_active_user_emails([])
    []
    """
    try:
        # Handle empty list
        if not users:
            return []

        active_user_emails = []

        # Collect emails from active users
        for user in users:
            try:
                # Check if user is active and has an email
                is_active = user.get("is_active", False)
                email = user.get("email")

                if is_active and email:
                    active_user_emails.append(email)
            except (KeyError, TypeError, AttributeError):
                # Skip users with invalid data
                continue

        return active_user_emails

    except Exception as e:
        print(f"error: unexpected error retrieving active user emails: {e}")
        return []


if __name__ == '__main__':
    # Call the refactored functions and display results
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
