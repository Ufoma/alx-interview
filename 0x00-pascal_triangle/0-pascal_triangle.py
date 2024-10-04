#!/usr/bin/python3
"""
Defines the function pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the given number of row count (n).
    
    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a row with 1 at either ends
        row = [1] * (i + 1)

        # Fill in the middle elements by adding values from the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
