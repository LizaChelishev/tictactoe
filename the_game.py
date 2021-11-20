import random

board = []
player1 = 'X'
player2 = 'O'


def print_board(board):
    # This function prints the board
    for i in range(3):
        row = []
    for j in range(3):
        row.append('_')
    board.append(row)


def players_turns():
    # This function announce the players
    print('Player 1: you play as X, player 2: you play as O')
    current_player = random.randint(0, 1)
    if current_player == 0:
        current_player = player1
    else:
        current_player = player2
    print('Player ' + current_player + ' this is your turn:')
    return current_player


def the_game(board, player1, player2, count):
    # This function decides which player is playing
    if count % 2 == 0:
        player = player1
    elif count % 2 == 1:
        player = player2


def not_valid(row, column):
    print("Invalid choice. Pick another one. ")


def is_filled(board, player1, player2, row, column):
    print("The square you picked is already filled. Pick another one.")

    # This is how you choose the filler in the board
    print("Player " + player + ", this is your turn. ")


def fix_spot(row, col, player):
    board[row][col] = player


row = int(input("Pick a row:"
                "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
column = int(input("Pick a column:"
                   "[left column: enter 0, middle column: enter 1, right column enter 2]:"))

# Now he check if players choice is valid
while (row > 2 or row < 0) or (column > 2 or column < 0):
    notValid(row, column)
    row = int(input("Pick a row[upper row:"
                    "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))

# We need to check if the place we chose was already chosen.
while (board[row][column] == player1) or (board[row][column] == player2):
    filled = isfilled(board, player1, player2, row, column)
    row = int(input("Pick a row[upper row:"
                    "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
