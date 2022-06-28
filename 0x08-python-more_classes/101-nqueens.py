#!/usr/bin/python3
"""
N-Queens Problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
"""
module var N board length
"""
N = 0
try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
else:
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


def safe(board, row, col, N):

    """ Check if placing is safe
    Args:
        board(list of lists): chess board
        row(int): placing row index
        col(int): placing col index
        N(int): check size
    """
    if any(i != 0 for i in board[row]):
        return False
    if any(R[col] != 0 for R in board):
        return False
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    r = row
    c = col
    while r >= 0 and c < N:
        if board[r][c] == 1:
            return False
        c += 1
        r -= 1
    r = row
    c = col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        c -= 1
        r += 1
    r = row
    c = col
    while r < N and c < N:
        if board[r][c] == 1:
            return False
        c += 1
        r += 1
    return True


def make_board(N):

    """ make board"""
    board = []
    row = []
    for i in range(N):
        for j in range(N):
            row.append(0)
        board.append(row)
        row = []
    return board


def print_board(board):

    """ print board"""
    N = len(board)
    sol = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                sol.append([i, j])
    print(sol)


solutions = []


def copy_board(board):

    sol = []
    r = []
    for row in board:
        for j in row:
            r.append(j)
        sol.append(r)
        r = []
    return sol


def solve(board, col, N):

    """ solve the board
    Args:
        board(list of lists): chess board
        col(int): placing col
        N(int): chess size
    """
    if col >= N:
        return True
    for row in range(N):
        if safe(board, row, col, N):
            board[row][col] = 1
            if solve(board, col + 1, N):
                solutions.append(copy_board(board))
            board[row][col] = 0
    return False


board = make_board(N)

solve(board, 0, N)
for i in range(len(solutions)):
    print_board(solutions[i])
