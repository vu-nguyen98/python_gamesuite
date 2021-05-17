# This file will process the words.txt that is used to populate hangman games
# The aim of this code is to process the listed words and:
# 1. Remove all words that are 3 letters or less.
# 2. Use an index to "rank" words based on difficulty of guessing
# 3. Split those words into 3 different .txt files: easy, medium and hard
# Difficulty based on the "A Better Hangman Strategy" found on https://datagenetics.com/blog/april12012/

# Import hangman since we are using a function from there
from hangman import word_split


# Function used to automatically assign difficulty numbers to each letter in the alphabet
# This is a pretty "caveman" way to assign difficulty points
# Essentially, each letter is weighted based on their probability of occurring in each word
# The list is found in "A Better Hangman Strategy" and compiled into a .txt file
# So, the most common letter (E) will be assigned 1, up to the least common letter (J), which is assigned 26
def populate_difficulty():
    difficulty_file = (open('hangman_word_probability.txt', 'r')).read()
    difficulty_file = difficulty_file.split('\n')

    # Initialize an empty dictionary to take in the difficulty number
    difficulty_dict = {}
    for z in range(len(difficulty_file)):
        difficulty_dict[(difficulty_file[z]).lower()] = int(z + 1)
    return difficulty_dict


# Reusing the API that is used to populate words
hangman_file = (open('words.txt', 'r')).read()
hangman_file = hangman_file.split('\n')

# Grab the difficulty list to process the difficulty
difficulty_dictionary = populate_difficulty()

# First, remove all of the words that are 4 letters or less
for x in hangman_file[:]:
    if len(x) <= 3:
        hangman_file.remove(x)

# Initialize the dictionary index
difficulty_index_dictionary = {}
for i in range(len(hangman_file)):
    # Reset difficulty points every iteration
    difficulty_points = 0
    broken_word = word_split(hangman_file[i])
    for j, k in difficulty_dictionary.items():
        for m in broken_word:
            if j == m:
                difficulty_points += k
    # Get the average difficulty of each of the word
    difficulty_points //= len(hangman_file[i])
    # Add the difficulty and the word to the difficulty dictionary
    difficulty_index_dictionary[hangman_file[i]] = difficulty_points

# Created a new list of sorted keys based on difficulty descending
sorted_keys = sorted(difficulty_index_dictionary, key=difficulty_index_dictionary.get, reverse=True)

# Open up three different files for writing, will be used for difficulty selection later
f_easy = open("words_easy.txt", "w")
f_medium = open("words_medium.txt", "w")
f_hard = open("words_hard.txt", "w")

for i in range(len(sorted_keys)):
    if i <= len(sorted_keys) / 3:
        f_hard.write(sorted_keys[i] + "\n")
    elif len(sorted_keys) / 3 < i < len(sorted_keys) / 3 * 2:
        f_medium.write(sorted_keys[i] + "\n")
    else:
        f_easy.write(sorted_keys[i] + "\n")
print("Job's done! Extracted words from words.txt, classified it based on length and difficulty.")
print("new word files are words_easy, words_medium and words_hard.")
f_easy.close()
f_medium.close()
f_hard.close()
