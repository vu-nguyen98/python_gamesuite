from array import *


def tictactoe_main():
    boardlist = []
    j = 4
    for i in range(j * j):
        boardlist.append('| ' + str(i+1) + ' |')
    index = 0
    for i in range(j*j):
        print(boardlist[i], end=" ")
        index += 1
        if index == j:
            print("\n")
            index = 0
    sel = input("Select a cell: ")
    customsel = '| ' + str(sel) + ' |'
    for i in range(len(boardlist)):
        if boardlist[i] == customsel:
            boardlist[i] = '| X |'
    for i in range(j*j):
        print(boardlist[i], end=" ")
        index += 1
        if index == 3:
            print("\n")
            index = 0

# TODO: Implement the game based on the idea above