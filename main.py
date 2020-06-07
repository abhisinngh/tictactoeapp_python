# global var
game_still_going = True
Winner = "A"

current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playGame():
    # this is where the game play begins
    displayBoard()
    while game_still_going:
        handleTurn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
         print(winner + " won")
    elif winner is None:
        print("Tie")


# handle a single turn of an arbitrary player
def handleTurn(player):
    print(player+"'s turn")
    position = input('choose position bw 1 to 9: ')
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("please give valid input bw 1-9 : ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("that's already taken , try diff ..")
    board[position] = current_player
    displayBoard()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    # check row
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def check_columns():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    if col2:
        return board[1]
    if col3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diag1 = board[0] == board[4] == board[7] != '-'
    diag2 = board[2] == board[4] == board[5] != '-'
    if diag1 or diag2:
        game_still_going = False
    if diag1:
        return board[0]
    if diag2:
        return board[2]

    return


playGame()
