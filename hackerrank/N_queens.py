# Neetcode question N queens:
# Given input n, return all the possible board states where
# n queens can be placed on the n x n board and they cannot
# attach each other.
# 1 <= n <= 8, time should be n! and space n^2.

from copy import deepcopy


def solve(n):
    ans = []

    # Returns a list of available column number for the next row
    def find_available_column_for_next_row(state):
        if len(state) == 0:
            return [i for i in range(n)]
        curr_r = len(state)
        impossible_c = set()
        ans = []
        for prev_r, prev_c in enumerate(state):
            impossible_c.add(prev_c)
            impossible_c.add(prev_c + curr_r - prev_r)  # diagonal right
            impossible_c.add(prev_c - (curr_r - prev_r))  # diagonal left

        for c in range(n):
            if c in impossible_c:
                continue
            ans.append(c)
        return ans

    # state is a list of int, each position represent the row number,
    # the value represent the column number.
    def backtrack(n, state):
        if len(state) == n:
            ans.append(deepcopy(state))
            return
        for c in find_available_column_for_next_row(state):
            state.append(c)
            backtrack(n, state)
            state.pop()

    backtrack(n, [])
    boards = []
    for state in ans:
        board = [["."] * n for i in range(n)]
        for r, c in enumerate(state):
            board[r][c] = "Q"
        boards.append(["".join(row) for row in board])
    return boards


def format_board(boards):
    print("#############################")
    if len(boards) == 0:
        print("No solution!!")
    for board in boards:
        for r in range(len(board)):
            print(board[r])
        print("###############################")


format_board(solve(2))  # impossible
format_board(solve(3))  # impossible
format_board(solve(4))  # possible
format_board(solve(5))  # 2
