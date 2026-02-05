"""
Lab 04: Data Structures

Implementations for the three required functions.
"""


def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function should take two lists and return a new list containing
    only the elements that are present in both input lists. The final
    list can be in any order.
    """
    # Use set intersection for efficiency and to remove duplicates
    if not list1 or not list2:
        return []
    return list(set(list1) & set(list2))


def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Convert the list to a dictionary keyed by username for O(1) lookups.
    """
    if not users:
        return None
    user_map = {user["name"]: user for user in users}
    return user_map.get(name)


def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.
    """
    return [n for n in numbers if n % 2 == 0]
