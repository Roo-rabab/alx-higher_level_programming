#!/usr/bin/python3
"""The N queens puzzle"""
import sys


def sa_fe(a, b, c):
    """checking if it's safe"""
    for x in range(c):
        if a[b][x] == 1:
            return False
    x = b
    y = c
    while x >= 0 and y >= 0:
        if a[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x = b
    y = c
    while x >= 0 and y >= 0:
        if a[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x = b
    y = c
    while x < len(a) and y >= 0:
        if a[x][y] == 1:
            return False
        x += 1
        y -= 1
    return True


def n_queens(a, c, sols):
    """solve the N queens problem"""
    z = len(a)
    if c == z:
        sol = []
        for i in range(z):
            for j in range(z):
                if a[i][j] == 1:
                    sol.append([i, j])
        sols.append(sol)
        return
    for i in range(z):
        if sa_fe(a, i, c):
            a[i][c] = 1
            n_queens(a, c + 1, sols)
            a[i][c] = 0


def solv_nqueens(z):
    """solve n queens"""
    a = [[0 for _ in range(z)] for _ in range(z)]
    sols = []
    n_queens(a, 0, sols)
    for sol in sols:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        z = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if z < 4:
        print("N must be at least 4")
        sys.exit(1)
    solv_nqueens(z)
