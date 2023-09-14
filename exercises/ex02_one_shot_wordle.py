"""EX02 - One-Shot Wordle."""
__author__ = "730662291"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while (len(word_guess) != len(secret_word)):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

index: int = 0
guess_outline: str = ""
while (index < len(secret_word)):
    if (secret_word[index] == word_guess[index]):
        guess_outline += GREEN_BOX
    else:
        guess_in_word: bool = False
        inner_index: int = 0
        while (guess_in_word != True and inner_index < len(secret_word)):
            if (word_guess[index] == secret_word[inner_index]):
                guess_in_word = True
            else:
                inner_index += 1
        if (guess_in_word): 
            guess_outline += YELLOW_BOX
        else:
            guess_outline += WHITE_BOX
    index += 1
print(guess_outline)

if (word_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")