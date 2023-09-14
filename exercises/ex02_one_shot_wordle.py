"""EX02 - One-Shot Wordle."""
__author__ = "730662291"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Declaring variable for the secret word and user's guess.
secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# If the guess isn't the same length as the secret word, keep asking the user for another guess.
while (len(word_guess) != len(secret_word)):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

index: int = 0
guess_outline: str = ""
# Traverses through each letter in secret word.
while (index < len(secret_word)):
    # Checks if the letter in the same position as guess and secret word are the same, if so concatonate a green box.
    if (secret_word[index] == word_guess[index]):
        guess_outline += GREEN_BOX
    else:
        guess_in_word: bool = False
        inner_index: int = 0
        # Goes through each letter in the secret word to see if the current letter from guess is in the secret word.
        while (not guess_in_word and inner_index < len(secret_word)):
            if (word_guess[index] == secret_word[inner_index]):
                guess_in_word = True
            else:
                inner_index += 1
        # If the current letter from guess is in the secret word, concatonate a yellow box.
        if (guess_in_word): 
            guess_outline += YELLOW_BOX
        # If the current letter from guess is not in the secret word, concatonate a white box.
        else:
            guess_outline += WHITE_BOX
    index += 1
# Outputs the outline for the user's guess.
print(guess_outline)

# If the guess is the same as the secret word, output a successful statement.
if (word_guess == secret_word):
    print("Woo! You got it!")
# If the guess is not the same as the secret word, output an unsuccessful statement.
else:
    print("Not quite. Play again soon!")