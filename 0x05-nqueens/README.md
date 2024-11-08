# N-Queens Solver

This Python program solves the **N-Queens puzzle**: placing `N` queens on an `N×N` chessboard so no two queens threaten each other. It uses a backtracking algorithm to find all possible solutions.

## Usage

Run the program from the command line:

```bash
./0-nqueens.py
```

- **`N`**: Integer for board size (`N ≥ 4`).

### Example
```bash
./0-nqueens.py
```

Output:
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each solution lists `[row, column]` positions for queen placements.

## Input Validation

The program checks:
- Exactly one argument is provided.
- `N` is an integer and `N ≥ 4`.

Errors:
- `Usage: nqueens N` if wrong number of arguments.
- `N must be a number` if `N` isn’t an integer.
- `N must be at least 4` if `N < 4`.
