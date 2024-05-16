import os
import random

def random_word(word_bank):
    return random.choice(word_bank)

def numplayers():
    while True:
        try:
            number_players = int(input("Enter the number of players: "))
            if number_players <= 0:
                print("There must be at least one player!")
                continue
            break
        except ValueError:
            print("Please enter a valid number of players!")
    return number_players

def letter_guess(chosen_word, guessed_letters):
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Only enter one letter.")
        return False
    
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'.")
        return False
        
    guessed_letters.add(guess)
    
    occurrences = chosen_word.count(guess)
    if occurrences > 0:
        print(f"You're getting closer! '{guess}' is in the word {occurrences} time(s)")
    else:
        print(f"Nice guess but '{guess}' isn't in the word.")
    return True

def word_guesses(chosen_word):
    guess = input("Guess the word: ").lower()

    if guess == chosen_word.lower():
        print("You got it! You got the word!!!")
        return True
    else:
        print("Nope, that's not it.")
        return False

def gameplay(word_bank):
    print("Welcome to the Word Guessing Game. The game will start. \n")
    num_players = numplayers
    chosen_word = random_word(word_bank)
    print("Your word has", len(chosen_word), "letters.")

    for player in range(1, num_players + 1):
        print("\nPlayer", player, "'s turn:")
        guessed_letters = set()
        guesses = 0

        while True:
            print("Current word:", " ".join([letter if letter in guessed_letters else "_" for letter in chosen_word]))

            guess_choice = input("Type 'letter to guess a letter or 'word' to guess the word: ")
            
            if guess_choice == "letter":
                if guess_choice(chosen_word, guessed_letters):
                    guesses +=1
            elif guess_choice == "word":
                if word_guesses(chosen_word):
                    guesses += 1
                    print("Number of guesses:", guesses)
                break
            else:
                print("Try again")


                
if __name__ == "__main__":
    word_bank = ["copper", "curse", "estate", "silver", "duchy", "gold", "province", "cellar", "market", "militia", "mine", "moat", "merchant", "remodel", "smithy", "village", "workshop", "festival", "laboratory", "sentry", "village", "chapel", "harbinger"]
    gameplay(word_bank)
