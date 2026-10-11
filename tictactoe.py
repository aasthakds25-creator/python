board = [" " for i in range(9)]

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner(p):
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]] == p:
            return True

    return False


def play():
    player = "X"

    for i in range(9):
        display()
        pos = int(input("Player " + player + ", enter position (1-9): ")) - 1

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid position!")
            continue

        board[pos] = player

        if winner(player):
            display()
            print("Player", player, "wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display()
    print("Game Draw!")


play()