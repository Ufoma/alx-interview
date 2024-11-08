#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    """
    for i in range(row):
        # Check for column and diagonal conflicts
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """
    Recursively place queens on the board and collect solutions.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1  # Backtrack

def nqueens(N):
    """
    Initialize the board and print all solutions to the N-Queens problem.
    """
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

def main():
    """
    Parse command-line arguments, validate input, and solve the N-Queens problem.
    """
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

    nqueens(N)

if __name__ == "__main__":
    main()

def main():
    """
    Parse command-line arguments, validate input, and solve the N-Queens problem.
    """
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

    nqueens(N)

if __name__ == "__main__":
    main()
