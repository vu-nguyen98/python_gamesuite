# Get all functions from util.py
# Get all functions from each of the individual games in the suit in other .py files
from hangman import *
from util import *

# Get some stuff going first, like making the option dictionary
options = dict([(1, 'Hangman'), (2, 'Tic Tac Toe'), (3, 'Shirotori (Word Game)')])

# Introduce the game interface
clear()
print("Welcome to the game suite")
print("We have the following games:")
for x in options:
    print("{0}. {1}".format(x, options[x]))

# Repeat this input loop until a valid selection is there
while True:
    sel = input("Please make your selection: ")
    if not sel:
        print("Please enter something!")
    elif int(sel) not in options:
        print("There is no such option!")
    else:
        break

if int(sel) == 1:
    hangman_main()
