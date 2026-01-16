def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def tic_tac_toe():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'

    for turn in range(9):
        display_board(board)

        while True:
            move = input(f"Player {current_player}, choose a position (1-9): ")
            if move.isdigit():
                move = int(move) - 1
                if 0 <= move <= 8 and board[move] not in ['X','O']:
                    board[move] = current_player
                    break
            print("❌ Invalid move. Try again.")

        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    display_board(board)
    print("🤝 It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()
