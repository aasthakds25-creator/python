# Tic Tac Toe Game in Python

# Create an empty 3 x 3 game board
board = [" " for _ in range(9)]


# Function to display the game board
def display_board():
    print()

    # Display first row
    print(board[0], "|", board[1], "|", board[2])

    print("--+---+--")

    # Display second row
    print(board[3], "|", board[4], "|", board[5])

    print("--+---+--")

    # Display third row
    print(board[6], "|", board[7], "|", board[8])

    print()


# Function to check whether a player has won
def check_winner(player):

    # All possible winning combinations
    winning_positions = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # Main diagonal
        (2, 4, 6)   # Other diagonal
    ]

    # Check every winning combination
    for a, b, c in winning_positions:

        # If all three positions contain the same player's symbol
        if board[a] == board[b] == board[c] == player:
            return True

    # No winning combination found
    return False


# Function to start and control the game
def play_game():

    # Player X starts the game
    current_player = "X"

    # Maximum 9 turns because the board has 9 positions
    for turn in range(9):

        # Display the current board
        display_board()

        # Ask the player to select a position
        position = int(input(
            f"Player {current_player}, enter position (1-9): "
        )) - 1

        # Check whether the position is valid
        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position! Try again.")
            continue

        # Place the player's symbol on the board
        board[position] = current_player

        # Check if the current player has won
        if check_winner(current_player):

            # Display the final board
            display_board()

            # Display the winner
            print(f"Player {current_player} Wins!")

            # End the game
            return

        # Change the player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # If all 9 positions are filled and nobody wins
    display_board()
    print("Game Draw!")


# Start the game
play_game()