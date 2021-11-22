def play_game():
    board = create_structure()
    print_the_board = print_board(board)
    player_1, player_2 = symbols_and_players()
    full = board_full(board, player_1, player_2)


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
    cols = len(board)
    print("    ")
    for r in range(rows):
        print(board[r][0], " , ", board[r][1], " , ", board[r][2])
        print("   ")
    return board


def symbols_and_players():
    # This function decides the symbols of the players
    player_1 = input("Player 1, do you want to be X or O? ")
    if player_1 == "X":
        player_2 = "O"
        print("Player 2, you are O. ")
    else:
        player_2 = "X"
        print("Player 2, you are X. ")
    return [player_1, player_2]


def choice_invalid(row, column):
    # This function tells the player that their selection is invalid
    print("Out of boarder. Pick another one. ")
    return None


def already_chosen(board, player_1, player_2, row, column):
    # This function tells the player that their selection was already chosen
    print("The square you picked is already filled. Pick another one.")
    return None


def start_the_game(board, player_1, player_2, moves):
    player = 0
    if moves % 2 == 0:
        player = player_2
    elif moves % 2 == 1:
        player = player_1
    print("Player " + player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    # Check if players' selection is valid
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        choice_invalid(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    # Check if the place you chose is already filled
    while (board[row][column] == player_1) or (board[row][column] == player_2):
        filled = already_chosen(board, player_1, player_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    # Locates player's symbol on the board
    if player == player_1:
        board[row][column] = player_1

    else:
        board[row][column] = player_2

    return board


def board_full(board, player_1, player_2):
    moves = 1
    winner = True
    # This function check if the board is full
    while moves < 10 and winner == True:
        start_game = start_the_game(board, player_1, player_2, moves)
        print_the_board = print_board(board)

        if moves == 9:
            print("The board is full. Game over.")
            if winner is True:
                print("Draw game. Start over.")

        winner = the_winner(board, player_1, player_2)
        moves += 1
    if winner is False:
        print("Game over.")
    return None


def the_winner(board, player_1, player_2):
    # This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == player_1:
            winner = False
            print("Player " + player_1 + ", you won!")

        elif board[row][0] == board[row][1] == board[row][2] == player_2:
            winner = False
            print("Player " + player_2 + ", you won!")

    # Check the columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == player_1:
            winner = False
            print("Player " + player_1 + ", you won!")
        elif board[0][col] == board[1][col] == board[2][col] == player_2:
            winner = False
            print("Player " + player_2 + ", you won!")

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == player_1:
        winner = False
        print("Player " + player_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == player_2:
        winner = False
        print("Player " + player_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_1:
        winner = False
        print("Player " + player_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_2:
        winner = False
        print("Player " + player_2 + ", you won!")

    return winner

play_game()
