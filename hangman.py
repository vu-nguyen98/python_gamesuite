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
    chosen_word_full = word_populate()
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
    while not (player_guessed):
        if player_life == 0:
            break
        # Print the player's progress
        print_player_guess_progress(player_guess_progress)
        print("\n")

        # Repeat this chunk of code until the player enters a valid letter in the English alphabet
        while True:
            print("You have {0} tries remaining...".format(player_life))
            player_guess = input("Please enter a letter: ")
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
            player_life -= 1

        # Run this every loop to determine if the player has guessed correctly
        if "_" not in player_guess_progress:
            player_guessed = True

    # When the loop breaks, check if the user has already guessed the word correctly
    # THen print corresponding comments
    if not player_guessed:
        print("Unfortunately, you have failed to guess the word in time!")
    else:
        print("You did it, you have guessed the word!")
    print("The word was {0}".format(chosen_word_full))


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


def print_player_guess_progress(guess_list):
    for x in guess_list:
        print(x, end=" ")
