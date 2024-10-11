def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the current player has won."""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Middle column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal \
        [board[2][0], board[1][1], board[0][2]]   # Diagonal /
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    """Check if the board is full (no empty spaces)."""
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move():
    """Get a valid move from the player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            return move
        except ValueError:
            print("Invalid move. Please enter a number between 1 and 9.")

def play_game():
    """Play a game of Tic-Tac-Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        move = get_move()
        row, col = divmod(move, 3)
        
        if board[row][col] != ' ':
            print("Cell already taken. Choose another one.")
            continue
        
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
