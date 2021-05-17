# Importing some libraries that we will be using for this specific game
import random
import itertools


def hangman_main():
    # Just introduction to the game
    print("Welcome to the game of hangman!")
    print("We will choose a random word for you. Please guess!")
    print("You will have six tries to guess the word.")

    # Now, we fetch a word to be used for hangman
    # Uses a function called word_populate to pick a random word in long list
    chosen_word = word_populate()
    # Then split the chosen word into letters
    chosen_word = word_split(chosen_word)
    # Then, create a "guessing" list for user based on length of chosen word
    player_guess_progress = []
    for _ in itertools.repeat(None, len(chosen_word)):
        player_guess_progress.append('_')

    # Now we begin the main game loop
    player_guessed = False
    while not (player_guessed):
        print_player_guess_progress(player_guess_progress)

        # Repeat this chunk of code until the player enters a valid letter in the English alphabet
        while True:
            player_guess = input("Please enter a letter")


def word_populate():
    # Open the words.txt file included in the folder
    # The words.txt file has a list of words that can be used in hangman
    hangman_file = (open("words.txt", "r")).read()

    # Since each word is in a line, split them by using newline (\n)
    # Now the hangman_file variable becomes a list
    hangman_file = hangman_file.split('\n')

    # Return a randomly chosen word in hangmanfile for the game
    return random.choice(hangman_file)


def word_split(word):
    return [char for char in word]


def print_player_guess_progress(list):
    for x in list:
        print(x, end=" ")
