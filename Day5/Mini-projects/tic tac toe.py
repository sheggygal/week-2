def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_input(player):
    while True:
        position = input(f"Player {player}, enter your position (row,col): ")
        row, col = position.split(",")
        row = int(row.strip()) - 1
        col = int(col.strip()) - 1

        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        else:
            print("Invalid position. Please enter row and column numbers between 1 and 3.")

def check_win(board, player):

    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return True

    return False

def play():

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    display_board(board)

    for _ in range(9):
        row, col = player_input(player)
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = player
        display_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print("It's a tie!")

play()