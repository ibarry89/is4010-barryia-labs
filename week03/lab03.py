import random


def generate_mad_lib(adjective, noun, verb):
    """Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped over the moon and giggled all the way home."
    """
    # Create a fun, easily testable story using f-string formatting
    story = (
        f"On a {adjective} afternoon, a {noun} {verb} through the town, "
        f"making everyone smile as it passed by. People talked about the {noun} for days."
    )
    return story


def guessing_game():
    """Plays a number guessing game with the user.

    The function generates a secret number between 1 and 100 (inclusive)
    and repeatedly prompts the user to guess until they find the number.
    It provides feedback on each guess and prints the number of attempts.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        attempts += 1
        guess_str = input("Enter your guess: ")
        try:
            guess = int(guess_str)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break


if __name__ == '__main__':
    guessing_game()
