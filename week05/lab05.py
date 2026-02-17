"""
Lab 05: functions and error handling

Refactored from the messy script into two functions:
- calculate_average_age(users)
- get_active_user_emails(users)

Includes basic error handling per lab instructions and a main block.
"""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
    {"name": "eve", "is_active": True, "email": "eve@example.com"},
]


def calculate_average_age(users_list):
    """Calculate the average age for users with valid integer ages.

    Parameters
    ----------
    users_list : list of dict
        List of user dictionaries which may contain an 'age' key.

    Returns
    -------
    float
        The average age as a float. Returns 0.0 if no valid ages are present
        or if an error occurs.
    """
    try:
        if not users_list:
            print("error: cannot calculate average age of an empty list.")
            return 0.0
        total_age = 0
        count = 0
        for user in users_list:
            try:
                age = user.get("age")
            except AttributeError:
                # user is not a dict-like object
                continue
            if isinstance(age, int):
                total_age += age
                count += 1
        if count == 0:
            print("error: cannot calculate average age of an empty list.")
            return 0.0
        return float(total_age) / float(count)
    except Exception as exc:
        print(f"error: unexpected error calculating average age: {exc}")
        return 0.0


def get_active_user_emails(users_list):
    """Return a list of emails for users who are active and have an email.

    Parameters
    ----------
    users_list : list of dict
        List of user dictionaries.

    Returns
    -------
    list of str
        Emails of active users. Returns an empty list if none found or on error.
    """
    emails = []
    try:
        if not users_list:
            return []
        for user in users_list:
            try:
                is_active = user.get("is_active")
                email = user.get("email")
            except AttributeError:
                # Skip items that aren't dict-like
                continue
            if is_active and email:
                emails.append(email)
        return emails
    except Exception as exc:
        print(f"error: unexpected error collecting active emails: {exc}")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
