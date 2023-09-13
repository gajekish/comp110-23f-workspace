"""Demonstrates while loops by finding lowest value in string"""

cards: str = "5235"

card_index: int = 0
low_card: int = cards[0]

#look at each number in the string
while card_index < 4:
    #check if current card is less than the low card
    current_card: int = cards[card_index]
    if (current_card < low_card):
        #update the value of the low card to be the value of our current card
        low_card = current_card
    card_index += 1
print(low_card)