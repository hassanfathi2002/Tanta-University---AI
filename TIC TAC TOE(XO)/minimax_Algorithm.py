# TEAM 11
# PROJECT : Tic-Tac-Toe Solver with Minimax and Memoization Optimization

best_move = {}  # Saves the best move for each state
best_val = {}  # Saves the best value for each state
next_turn = {'X': 'O', 'O': 'X'}  # Dictionary to switch turns between players

def print_grid(grid):
    """
    Prints the Tic-Tac-Toe grid in a 3x3 format.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.
    """
    print("")
    for i in range(9):
        print(f" {grid[i]} ", end='')
        if i % 3 != 2:  # Print '|' except at the end of the row
            print("|", end='')
        if i % 3 == 2 and i != 8:  # Print row separator except after the last row
            print("\n---+---+---")
    print("\n")

def check_winner(grid):
    """
    Checks if there is a winner in the current grid.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.

    Returns:
        str: 'X' if player X wins, 'O' if player O wins, '-' if there is no winner yet.
    """
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for player in ['X', 'O']:
        for pattern in win_patterns:
            count = 0
            for i in pattern:
                count += (grid[i] == player)
            if count == 3:
                return player
    return '-'

def save_grid(grid, pos, val):
    """
    Saves the best move and its value for the given grid state.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.
        pos (int): The best move position.
        val (int): The value of the best move.
    """
    best_move[tuple(grid)] = pos
    best_val[tuple(grid)] = val

def get_best_move(grid):
    """
    Retrieves the best move for the given grid state.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.

    Returns:
        int: The best move position.
    """
    return best_move[tuple(grid)]

def get_best_val(grid):
    """
    Retrieves the best value for the given grid state.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.

    Returns:
        int: The value of the best move.
    """
    return best_val[tuple(grid)]

def is_grid_solved(grid):
    """
    Checks if the current grid state has been solved and stored.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.

    Returns:
        bool: True if the grid state is solved, False otherwise.
    """
    return tuple(grid) in best_move

def minimax(grid, player):
    """
    Implements the minimax algorithm with memoization to find the best move.

    Args:
        grid (list): A list of 9 elements representing the Tic-Tac-Toe grid.
        player (str): The current player ('X' or 'O').

    Returns:
        int: The value of the best move.
    """
    if is_grid_solved(grid):
        return get_best_val(grid)

    if check_winner(grid) != '-':
        return 1 if check_winner(grid) == 'X' else -1

    best_pos = -1
    best_val = -10 if player == 'X' else 10

    for i in range(9):
        if grid[i] == str(i + 1):  # If the cell is empty (represented by its index)
            grid[i] = player  # Make the move
            cur_val = minimax(grid, next_turn[player])  # Recursively evaluate the move
            if (best_val < cur_val) == (player == 'X'):
                # if player == x then maxmimize
                # if player == o then minimize
                best_val = cur_val
                best_pos = i
            grid[i] = str(i + 1)  # Undo the move

    if best_pos == -1:
        best_val = 0  # If no moves left, it's a tie

    save_grid(grid, best_pos, best_val)  # Save the result for memoization
    return best_val

def main():
    """
    The main function to play the Tic-Tac-Toe game against an AI using the minimax algorithm.
    """
    grid = list("123456789")  # Initialize the grid with positions
    minimax(grid, 'X')  # try all possibilities

    user = '?'
    while True:
        user = input("X or O ? ")
        if user == 'X' or user == 'O':
            break

    for turn in range(9):
        # User's turn
        if (turn % 2 == 0) == (user == 'X'):
            # if user == x and turn == 0 , 2 , 4 , 6 , 8
            # if user == o and turn == 1 , 3 , 5 , 7
            while True:
                if turn == 0:  # first turn
                    print_grid(grid)
                pos = input("Your move, Enter a valid position : ")
                if pos >= '1' and pos <= '9':
                    pos = int(pos) - 1
                    if grid[pos] == str(pos + 1):
                        grid[pos] = user
                        break
            print("Your move")
            print_grid(grid)
        # AI's turn
        else:
            cur_move = get_best_move(grid)  # Get the best move in time complexity O(1) !!
            grid[cur_move] = next_turn[user]
            print("AI move ")
            print_grid(grid)

        if check_winner(grid) != '-':
            if check_winner(grid) == user:
                print("Congrats, You defeated AI")  # impossible
            else:
                print("Noob, AI smashed you")
            break

        elif turn == 8:  # No moves left
            print("GAME is draw, your IQ is great as 10^8 operation in second's processor")

if __name__ == '__main__':
    main()
