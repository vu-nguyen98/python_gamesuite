# Importing some libraries that we will be using for this specific game
import itertools
import random
import time

from util import *


def word_populate(diff):
    # Open the different .txt file included in the folder
    # The words.txt file has a list of words that can be used in hangman
    # Through processing of words.txt, words_easy.txt, words_medium.txt and words_hard.txt are created
    # These will allow for difficulty selection

    # If argument passed in is 1 -> easy, 2 -> medium and 3 -> hard
    if int(diff) == 1:
        hangman_file = (open("words_easy.txt", "r")).read()
    elif int(diff) == 2:
        hangman_file = (open("words_medium.txt", "r")).read()
    else:
        hangman_file = (open("words_hard.txt", "r")).read()

    # Since each word is in a line, split them by using newline (\n)
    # Now the hangman_file variable becomes a list
    hangman_file = hangman_file.split('\n')

    # Return a randomly chosen word in hangman_file for the game
    return random.choice(hangman_file)


def word_split(word):
    return [char for char in word]


def print_player_guess_progress(guess_list):
    for x in guess_list:
        print(x, end=" ")


def hangman_main():
    # Wrap entire body of the program in a while statement to allow for continuous gameplay
    while True:
        # Just introduction to the game
        clear()
        print("Welcome to the game of hangman!")
        print("We will choose a random word for you. Please make guesses!")
        print("You will have six tries to guess the word.\n")

        # Allow for difficulty selection
        print("But first, please select the difficulty that you want:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        # Repeat this until the player selects a proper difficulty
        while True:
            diff_sel = input("Your choice: ")
            if not diff_sel:
                print("Please enter something!")
            elif int(diff_sel) not in (1, 2, 3):
                print("Please select a proper difficulty! 1 for easy, 2 for medium, 3 for hard!")
            else:
                break

        # Now, we fetch a word to be used for hangman
        # Uses a function called word_populate to pick a random word in long list
        chosen_word_full = word_populate(diff_sel)
        # Then split the chosen word into letters
        chosen_word = word_split(chosen_word_full)
        # Then, create a "guessing" list for user based on length of chosen word
        player_guess_progress = []
        for _ in itertools.repeat(None, len(chosen_word)):
            player_guess_progress.append('_')

        # Now we begin the main game loop
        # Instantiate the player have guessed, player life remaining, and "memory" list of words guessed
        player_guessed = False
        player_life = 6
        guess_memory = []

        # Repeat this as long as the player still has not guessed the correct answer
        while not player_guessed:
            if player_life == 0:
                break
            # Print the player's progress
            clear()
            print_player_guess_progress(player_guess_progress)
            print("\n")
            # Run this every loop to determine if the player has guessed correctly
            if "_" not in player_guess_progress:
                player_guessed = True
                break

            # Repeat this chunk of code until the player enters a valid letter in the English alphabet
            while True:
                print("You have {0} tries remaining...".format(player_life))
                print("Letters that you have already guessed:", end=" ")
                for i in guess_memory:
                    print(i, end=" ")
                player_guess = input("\nPlease enter a letter: ")
                if not player_guess.isalpha():
                    print("You must guess an alphabetical letter!\n")
                elif len(player_guess) > 1:
                    print("Your guess is too long! Guess only one letter!\n")
                elif player_guess in guess_memory:
                    print("You already guessed this one! Try another guess!\n")
                else:
                    break

            # If input is valid, append the letter into a "memory" list to prevent dupes
            guess_memory.append(player_guess)

            # Now, determine if the guessed letter matches anything in the word
            # Use i as an index to determine position in the list
            # Also use correct_guess to flag if the player guessed at least one letter correctly
            i = 0
            correct_guess = False
            # Use for to run through the chosen word letter by letter
            for x in chosen_word:
                # If the guess is correct then change the letter at the position determined by i
                # This will allow for the printing of the player's progress
                if player_guess.lower() == x:
                    player_guess_progress[int(i)] = x
                    correct_guess = True
                i += 1

            if not correct_guess:
                print("No match! You lost a life!")
                time.sleep(1)
                player_life -= 1

        # When the loop breaks, check if the user has already guessed the word correctly
        # Then print corresponding comments
        if not player_guessed:
            print("Unfortunately, you have failed to guess the word in time!")
        else:
            print("You did it, you have guessed the word!")
        print("The word was {0}".format(chosen_word_full))
        time.sleep(1)
        print("Would you like to play another game, or return to the main menu?")
        print("Type y to return to main menu, or anything else if you want to play another game.")
        cont_sel = input("Your selection: ")
        if cont_sel == "y":
            return
