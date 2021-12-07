# Python v3.9.5

# Generate a new tic-tac-toe board
# RETURN: A 3x3 matrix reprsenting the board
def new_board():
    return [[None, None, None], [None, None, None], [None, None, None]]


# Pretty-print the board to terminal
# board: Tic-tac-toe board
def render(board):
    str_board = "  0 1 2 \n -------\n"
    for row in range(len(board)):
        str_board += str(row) + "|"
        for col in range(len(board[row])):
            if board[row][col]:
                str_board += board[row][col] + " "
            else:
                str_board += "  "
        str_board = str_board[:-1] + "|\n"
    str_board += " -------\n"

    print(str_board)


# Get the player's next move
# RETURN: Co-ordinates of the next move as a tuple
def get_move():
    x = input("What is your move's X co-ordinate?: ")
    y = input("What is your move's Y co-ordinate?: ")

    return (int(x), int(y))


# Update the board with the latest move
# PRECONDITION: Pos is a legal move
# pos: Position of latest move
# board: Tic-tac-toe board
# player: The ID of the player who made the turn
# RETURN: Updated board
def make_move(pos, board, player):
    board[pos[1]][pos[0]] = player

    return board


# Check if a player's move is valid
# board: Tic-tac-toe board
# pos: Position of latest move
# RETURN: True if valid move, False otherwise
def is_valid_move(board, pos):
    if board[pos[1]][pos[0]]:
        return False
    else:
        return True


# Switch who's turn it currently is
# current: Current player ID
# RETURN: Next player ID
def switch_players(current):
    if current == "X":
        return "O"
    else:
        return "X"


# Check if a player has won
# board: Tic-tac-toe board
# RETURN: ID of the player who won, None if no winner
def get_winner(board):
    lines = [
        board[0],
        board[1],
        board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    for line in lines:
        if line[0] == line[1] and line[1] == line[2]:
            if line[0] == "X":
                return "X"
            elif line[0] == "O":
                return "O"
            else:
                continue
    
    return None


# Check if game has ended in a draw
# board: Tic-tac-toe board
# RETURN: True if a draw, False otherwise
def is_draw(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if not board[row][col]:
                return False
    
    return True


# Main
if __name__ == "__main__":
    current_player = "X"
    board = new_board()
    render(board)

    while True:
        move_coords = get_move()

        if not is_valid_move(board, move_coords):
            print("Invalid move: ({0}, {1}) is already taken!".format(move_coords[0], move_coords[1]))
            continue

        board = make_move(move_coords, board, current_player)
        render(board)
        current_player = switch_players(current_player)

        winner = get_winner(board)
        if winner:
            print("Player {} has won!".format(winner))
            break
        elif is_draw(board):
            print("Game has ended in a draw!")
            break
