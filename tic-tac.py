def displayBoard(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def player_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter col (0, 1, or 2): "))

            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("invalid input")

        except ValueError:
            print("Input Invalid, enter Valid input")


def make_move(board, row, col, current_player):
    if board[row][col] == ' ':
        board[row][col] = current_player
        return True
    else:
        print("Cell is taken already")
        return False


def check_winner(board, current_player):
    for i in range(3):
        if all(board[i][j] == current_player for j in range(3)) or all(board[j][i] == current_player for j in range(3)):
            return True
    if all(board[i][i] == current_player for i in range(3)) or all(board[i][2-i] == current_player for i in range(3)):
        return True
    return False


def main():
    board = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

    current_player = 'X'

    for i in range(9):
        displayBoard(board)
        print(f"Player {current_player}'s Turn: ")

        row, col = player_move()

        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                displayBoard(board)
                print(f"{current_player} wins!")
                break

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = "X"

        else:
            i -= 1

    else:
        displayBoard(board)
        print("its a tie!")


main()