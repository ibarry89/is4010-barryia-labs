import json


def save_contacts_to_json(contacts, filename):
    """
    Saves a list of contacts (dictionaries) to a file in JSON format.

    Parameters
    ----------
    contacts : list
        A list of contact dictionaries.
    filename : str
        The name of the file to save the contacts to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def load_contacts_from_json(filename):
    """
    Loads a list of contacts from a JSON file.

    Parameters
    ----------
    filename : str
        The name of the file to load contacts from.

    Returns
    -------
    list
        A list of contact dictionaries. Returns an empty list if the
        file does not exist.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    contacts_file = "contacts.json"

    my_contacts = load_contacts_from_json(contacts_file)
    print(f"Loaded {len(my_contacts)} contact(s).")

    new_contact = {"name": "Charles Babbage", "email": "charles@computers.org"}
    my_contacts.append(new_contact)
    print(f"Added a new contact for {new_contact['name']}.")

    save_contacts_to_json(my_contacts, contacts_file)
    print("Saved contacts to disk.")