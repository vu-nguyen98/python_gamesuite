class Player:
    def __init__(self, icon):
        self.icon = icon


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
    player = Player(icon_sel)

    while True:
        print_board(ttt_board)
        row = input("Pick row: ")
        col = input("Pick column: ")
        ttt_board[(int(row-1))][(int(col-1))] = player.icon
        print_board(ttt_board)
        break

# TODO: Implement the game based on the idea above
