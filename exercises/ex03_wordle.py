"""EX03 - Structured Wordle."""
__author__ = "730662291"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Returns True if char is in word and False if not."""
    assert len(char) == 1
    index = 0
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
    while (inner_index < len(secret)):
        if (secret[inner_index] == guess[inner_index]):
            guess_outline += GREEN_BOX
        elif contains_char(secret, guess[inner_index]):
            guess_outline += YELLOW_BOX
        else:
            guess_outline += WHITE_BOX
        inner_index += 1
    return guess_outline


def input_guess(expected_length: int) -> str:
    """Returns a guess with an expected length of characters."""
    word_guess: str = input(f"Enter a {expected_length} character word: ")
    while (len(word_guess) != expected_length):
        word_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    victory: bool = False
    while (not victory and turns < 7):
        print(f"=== Turn {turns}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        if (user_guess == secret_word):
            print(emojified(user_guess, secret_word))
            victory = True
        else:
            print(emojified(user_guess, secret_word))
            turns += 1
    if (victory):
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()