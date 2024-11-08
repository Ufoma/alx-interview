#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.

    Args:
        board (list): Current state of the board, where board[i] is the column
                      position of the queen in row i.
        row (int): The current row to place a queen.
        col (int): The current column to place a queen.

    Returns:
        bool: True if no other queens can attack this position, False otherwise.
    """
    for i in range(row):
        # Check same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """
    Recursively solve the N-Queens problem by placing queens row by row.

    Args:
        board (list): Current state of the board.
        row (int): The row where we are trying to place a queen.
        N (int): The size of the chessboard (N x N).
        solutions (list): List to store all valid solutions found.

    Returns:
        None. Solutions are added to the solutions list.
    """
    # Base case: if all queens are placed, store the solution
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    # Try placing queen in each column of the current row
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col  # Place queen
            solve_nqueens(board, row + 1, N, solutions)  # Recurse to the next row
            board[row] = -1  # Remove queen (backtrack)

def nqueens(N):
    """
    Find all solutions to the N-Queens problem for a given board size.

    Args:
        N (int): The size of the chessboard (N x N).

    Prints:
        Each solution as a list of [row, column] pairs for the queen positions.
    """
    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    solutions = []  # List to store all solutions
    solve_nqueens(board, 0, N, solutions)  # Start solving from row 0

    # Print each solution
    for solution in solutions:
        print(solution)

def main():
    """
    Parse command-line arguments, validate input, and solve the N-Queens problem.

    Exits with a status code of 1 if there's an invalid input.
    """
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Run the N-Queens solution
    nqueens(N)

if __name__ == "__main__":
    main()
    
