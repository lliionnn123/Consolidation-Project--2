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

def letter_guess(chosen_word, guessed_letters, display_word):
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Only enter one letter.")
        return False
    
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'.")
        return False
        
    guess_found = False
    for i in range(len(chosen_word)): 
        letter = chosen_word[i]
        if letter.lower() == guess:
            print(f"You're getting closer! '{guess}' is in the word.")
            display_word[i] = guess
            guess_found = True

    if not guess_found:
        print(f"Nice try but '{guess}' is not in the word.")
        return True

def word_guesses(chosen_word, num_guesses):
    guess = input("Guess the word: ").lower()

    if guess == chosen_word.lower():
        print("You got it! You got the word!!!")
        return True, num_guesses
    else:
        print("Nope, that's not it.")
        return False, num_guesses + 1

def gameplay(num_players, word_bank, display_word):
    print("Welcome to the Word Guessing Game. The game will start. \n")
    chosen_word = random_word(word_bank)
    print("Your word has", len(chosen_word), "letters.")

    display_word = ["_" for _ in chosen_word]

    player_scores = {i + 1: {"guessed_letters": set(), "guesses": 0} for i in range(num_players)}

    while True:
        for player in player_scores.keys():
            print("\nPlayer", player, "'s turn:")
            print("Current word: ", " ".join([letter if letter in player_scores[player]["guessed_letters"] else "_" for letter in display_word]))

            guess_choice = input("Type out the word 'letter' to guess a letter or 'word' to guess the word: ").lower()

            if guess_choice == "letter":
                if letter_guess(chosen_word, player_scores[player]["guessed_letters"], display_word):
                    player_scores[player]["guesses"] += 1
            elif guess_choice == "word":
                guess_result, player_scores[player]["guesses"] = word_guesses(chosen_word, player_scores[player]["guesses"])
                if guess_result:
                    return
                if player_scores[player]["guesses"] >= 3:
                    print("Uh oh! You reached the maximum amount of guesses. You lost!")
                    return
            else:
                print("Try again.")
                
if __name__ == "__main__":
    num_players = numplayers()
    word_bank = ["Copper", "Curse", "Estate", "Silver", "Duchy", "Gold", "Province", "Cellar", "Market", "Militia", "Mine", "Moat", "Merchant", "Remodel", "Smithy", "Village", "Workshop", "Festival", "Laboratory", "Sentry", "Village", "Chapel", "Harbinger"]
    display_word = list(random_word(word_bank))
    gameplay(num_players, word_bank, display_word)
