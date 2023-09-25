"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730662291"

five_character_word: str = input("Enter a 5-character word: ")

if (len(five_character_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ") 

if (len(character) != 1):
    print("Error: Character must be a single character")
    exit()

counter: int = 0
print("Searching for " + character + " in " + five_character_word)

if (character == five_character_word[0]):
    print(character + " found at index 0")
    counter += 1
if (character == five_character_word[1]):
    print(character + " found at index 1")
    counter += 1
if (character == five_character_word[2]):
    print(character + " found at index 2")
    counter += 1
if (character == five_character_word[3]):
    print(character + " found at index 3")
    counter += 1
if (character == five_character_word[4]):
    print(character + " found at index 4")
    counter += 1

if (counter == 0):
    print("No instances of " + character + " found in " + five_character_word)
if (counter == 1):
    print("1 instance of " + character + " found in " + five_character_word)
else:
    print(str(counter) + " instances of " + character + " found in " + five_character_word)
