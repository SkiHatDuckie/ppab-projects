# Python v3.9.5

import random
import math
import time


# Generate a board state where every cell is either assigned as alive or dead
# 1 = alive
# 0 = dead
# width: Width of the board
# height: Height of the board
# RETURN: The initial board state
def random_state(width, height):
    board = []
    for i in range(height):
        board.append([])
        for _ in range(width):
            board[i].append(math.floor(random.random() * 2))

    return board


# Format the board state and print it to the terminal
# board: Board state
def render(board):
    str_board = str.join("", ["-" for _ in range(len(board[0]) + 2)]) + "\n"
    for row in range(len(board)):
        str_board += "|"
        for col in range(len(board[row])):
            if board[row][col] == 1:
                str_board += "#"
            else:
                str_board += " "
        str_board += "|\n"
    str_board += str.join("", ["-" for _ in range(len(board[0]) + 2)])
        
    print(str_board)


# Check for state of neighbors surrounding a given cell
# board: Board state
# row: Row of given cell
# col: Col of given cell
# RETURN: Number of alive cells neighboring given cell
def check_neighbors(board, row, col):
    alive = 0
    if col != 0:
        if row != 0 and board[row - 1][col - 1] == 1:
            alive += 1
        if row + 1 < len(board) and board[row + 1][col - 1] == 1:
            alive += 1
        if board[row][col - 1] == 1:
            alive += 1
    if col + 1 < len(board[0]):
        if row != 0 and board[row - 1][col + 1] == 1:
            alive += 1
        if row + 1 < len(board) and board[row + 1][col + 1] == 1:
            alive += 1
        if board[row][col + 1] == 1:
            alive += 1
    if row != 0 and board[row - 1][col] == 1:
        alive += 1
    if row + 1 < len(board) and board[row + 1][col] == 1:
        alive += 1
    
    return alive


# Calculate the next state of the board
# board: Board state
# RETURN: New board state
def next_board_state(board):
    new_board = board
    for row in range(len(board)):
        for col in range(len(board[row])):
            alive = check_neighbors(board, row, col)
            if alive < 2 or alive > 3:
                new_board[row][col] = 0
            elif alive == 3:
                new_board[row][col] = 1
    
    return new_board


# Main
if __name__ == "__main__":
    board_state = random_state(100, 10)
    while True:
        render(board_state)
        board_state = next_board_state(board_state)
        time.sleep(1)
