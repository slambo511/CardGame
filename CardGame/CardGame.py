# Imports go at the top
import csv
import random

#'The game uses a deck of cards. There are 30 cards in a deck. 
# Each card has one colour (red, black or yellow). Each card has 
# a number (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) for each colour. Each card 
# is unique.

# Create the deck using lists to hold the values
red_cards = ["Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9", 
             "Red 10"]
black_cards = ["Black 1", "Black 2", "Black 3", "Black 4", "Black 5", "Black 6", "Black 7", 
               "Black 8", "Black 9", "Black 10"]
yellow_cards = ["Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", 
                "Yellow 7", "Yellow 8", "Yellow 9", "Yellow 10"]
deck = [red_cards, black_cards, yellow_cards]

for cards in deck:
    for card in cards:
        print(str(card))

