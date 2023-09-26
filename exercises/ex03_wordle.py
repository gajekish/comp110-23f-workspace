"""EX03 - Structured Wordle."""
__author__ = "730662291"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Returns True if char is in word and False if not."""
    assert len(char) == 1
    index = 0
    # Loops through the secret word and returns true if the given character is in the word, otherwise returns false.
    while (len(word) > index):
        if (word[index] == char):
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a codified string with colors depending on the index of the letters in secret and guess."""
    assert len(guess) == len(secret)
    guess_outline: str = ""
    inner_index: int = 0
    # Appends green, yellow, or white boxes to an outline depending on the characters in secret and guess.
    while (inner_index < len(secret)):
        # If the letter in the same index as secret and guess is the same, append a green box.
        if (secret[inner_index] == guess[inner_index]):
            guess_outline += GREEN_BOX
        # If the letter from guess is in the secret word, append a yellow box. Calls to the contains_char() function to check this.
        elif contains_char(secret, guess[inner_index]):
            guess_outline += YELLOW_BOX
        # If the letter in the same index as secret and guess is not the same nor in the secret word, append a white box.  
        else:
            guess_outline += WHITE_BOX
        inner_index += 1
    # Returns the emoji outline of the boxes after every letter in guess is checked with the secret word.
    return guess_outline


def input_guess(expected_length: int) -> str:
    """Returns a guess with an expected length of characters."""
    # Asks the user for input given the criteria that it must be a certain character length.
    word_guess: str = input(f"Enter a {expected_length} character word: ")
    # Checks to see if the user input matches the given criteria. If not, ask the user again.
    while (len(word_guess) != expected_length):
        word_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Initializes key variables for the Wordle program to operate properly.
    secret_word: str = "codes"
    turns: int = 1
    victory: bool = False
    # Game will continue if the user does not guess the word and has 6 tries to do so.
    while (not victory and turns < 7):
        print(f"=== Turn {turns}/6 ===")
        # Asks the user for their guess. Calls to the input_guess() function to verify if it matches the length of the secret word.
        user_guess: str = input_guess(len(secret_word))
        # If the guess and secret word are the same, the user wins and their guess outline will be outputted. Calls to the emojified() function to create the outline.
        if (user_guess == secret_word):
            print(emojified(user_guess, secret_word))
            victory = True
        # If the guess and secret word are not the same, their guess outline will be outputted and will continue to their next turn. Calls to the emojified() function to create the outline.
        else:
            print(emojified(user_guess, secret_word))
            turns += 1
    # When the user wins, a certain message will be outputted telling them how many turns it took them to win.
    if (victory):
        print(f"You won in {turns}/6 turns!")
    # If the user does not win, a certain message will be outputted.
    else:
        print("X/6 - Sorry, try again tomorrow!")

# Makes it possible to run this Wordle program as a module and for other modules to import this to reuse.
if __name__ == "__main__":
    main()