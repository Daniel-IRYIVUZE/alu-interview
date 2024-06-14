#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The size of the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
        triangle (list): Pascal's triangle represented as a list of lists.

    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


# Test the function
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
