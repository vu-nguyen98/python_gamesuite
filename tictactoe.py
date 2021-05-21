# Class that represents the players (including bots)
from itertools import *


class Player:
    def __init__(self, icon):
        self.icon = icon


# Class that represents the game, tracks turn count and whatnot
class Game:
    def __init__(self, player_turn):
        self.player_turn = player_turn


# Function to create a new board
def create_board(rows, cols):
    return [["| |" for i in range(cols)] for j in range(rows)]


# Function to print the board every "turn" of the game
def print_board(arr):
    for row in arr:
        index = 0
        for col in row:
            print(col, end="  ")
            index += 1
            if index == len(col):
                print('\n')


def horizontal_check(arr):
    for row in arr:
        count = 0
        for col in row:
            if col != '| |':
                count += 1
                if count == 3:
                    return True
    return False


def vertical_check(arr):
    counter = 0
    for a in range(len(arr)):
        counter = ([row[a] for row in arr]).count('| |')
        if counter == 0:
            return True
    return False


def diagonal_check(arr):
    counter = 0
    for a in range(3):
        for b in range(3):
            if arr[a][b] != '| |':
                counter += 1
    if counter == 3:
        return True
    counter = 0
    for a in range(2):
        for b in range(2, -1, -1):
            if arr[a][b] != '| |':
                counter += 1
    if counter == 3:
        return True
    return False


def check_game_condition(ttt_board):
    return horizontal_check(ttt_board) or vertical_check(ttt_board) or diagonal_check(ttt_board)


def tictactoe_main():
    print("Welcome to the tic-tac-toe game!")
    print("Get ready to create 3 in a row and win!")

    # Call the function to create the board
    ttt_board = create_board(3, 3)

    print("Instead of the normal noughts and crosses, we allow for you to customize yourself!")
    print("Just enter any letter in the alphabet!")
    while True:
        icon_sel = input("Enter your letter: ")
        break
    icon_sel = "|" + icon_sel.upper() + "|"
    # Give the player the icon that they wanted to have
    player = Player(icon_sel)
    # Establish new game
    new_game = Game(True)

    while True:
        print_board(ttt_board)
        # If the player turn is true, then allow for player to make a move
        if new_game.player_turn:
            row = input("Pick row: ")
            col = input("Pick column: ")
            ttt_board[(int(row) - 1)][(int(col) - 1)] = player.icon
        # Every loop, check if the game is over
        game_over = diagonal_check(ttt_board)
        print(game_over)

# TODO: Implement the game based on the idea above
