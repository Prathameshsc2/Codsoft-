import random

# Constants for player and AI
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw condition)
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm to determine the best move for the AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, PLAYER):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# Function to find the best move for the AI
def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Function for player's move
def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter row and column as integers between 0 and 2.")

# Main game loop
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        player_move(board)
        print_board(board)
        if check_winner(board, PLAYER):
            print("Player wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is making its move...")
        row, col = best_move(board)
        board[row][col] = AI
        print_board(board)
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
