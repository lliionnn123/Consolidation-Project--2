import os
import random

name = input("Choose your name:")

print("Welcome to the Word Guessing Game. The game will start", name)

word_bank = ["Copper", "Curse", "Estate", "Silver", "Duchy", "Gold", "Province", "Cellar", "Market", "Militia", "Mine", "Moat", "Merchant", "Remodel", "Smithy", "Village", "Workshop", "Festival", "Laboratory", "Sentry", "Village", "Chapel", "Harbinger"]

def random_word(word_bank):
    return random.choice(word_bank)

def gameplay():
    chosen_word = word_bank()

    while True:
        try:
            number_players = int(input("Enter the number of players: "))
            if number_players <= 0:
                print("There must be at least one player!")
                continue
            break
        except ValueError:
            print("Please have at least one player!")

    players = []
    for i in range(number_players):
        players.append("Player " + str(i + 1))
