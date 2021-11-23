def play_game():
    board = create_structure()
    print_board(board)
    player_1, player_2 = symbols_and_players()
    run_game(board, player_1, player_2)


def number_of_rows(board):
    return len(board)


def number_of_columns(board):
    return len(board[0])


def create_structure():
    # This function creates athe structure of the board
    print("Here is the board: ")
    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
    return board


def print_board(board):
    # This function prints the board
    rows = len(board)
    cols = len(board[0])
    print("")
    for r in range(rows):
        for c in range(cols):
            print(board[r][c], end='')
            if c != len(board[0]) - 1:
                print(" , ", end='')
        print("\n")


def symbols_and_players():
    player_1 = "X"
    player_2 = "O"
    return player_1, player_2


def choice_invalid():
    # This function tells the player that their selection is invalid
    print("Out of board. Pick another one. ")


def already_chosen():
    # This function tells the player that their selection was already chosen
    print("The square you picked is already filled. Pick another one.")


def get_current_player(moves, player_1, player_2):
    if moves % 2 == 0:
        player = player_2
    elif moves % 2 == 1:
        player = player_1
    return player


def is_users_input_valid(board, row, column):
    is_valid = False
    if (number_of_rows(board) - 1 >= row >= 0) and (number_of_columns(board) - 1 >= column >= 0):
        if board[row][column] == '_':
            is_valid = True
        else:
            already_chosen()
    else:
        choice_invalid()
    return is_valid


def start_the_game(board, player):
    print("Player " + player + ", it is your turn.")

    # Check if the players choice is valid
    while True:
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))
        if is_users_input_valid(board, row, column) is True:
            break

    # Locates player's symbol on the board
    board[row][column] = player

    return board


def run_game(board, player_1, player_2):
    moves = 1
    winner = False
    number_of_board_positions = number_of_rows(board) * number_of_columns(board)
    while moves < number_of_board_positions + 1 and winner is False:
        player = get_current_player(moves, player_1, player_2)
        start_the_game(board, player)
        print_board(board)

        if moves == number_of_board_positions:
            print("The board is full. Game over.")
            if winner is False:
                print("Draw game. Start over.")

        winner = the_winner(board, player_1)
        if winner is False:
            winner = the_winner(board, player_2)

        moves += 1
    if winner is True:
        print("Game over.")


def the_winner(board, player):
    # This function checks if any winner is winning
    winner = False
    # Check the rows
    for row in range(0, len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            winner = True
            print("Player " + player + ", you won!")
            return winner

    # Check the columns
    for col in range(0, len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            winner = True
            print("Player " + player + ", you won!")
            return winner

    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        winner = True
        print("Player " + player + ", you won!")

    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        winner = True
        print("Player " + player + ", you won!")

    return winner


play_game()
