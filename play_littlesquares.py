# Topcoder quesition.

from copy import deepcopy

state0 = ["..", ".."]  # first wins

state1 = ["...##", "..###"]  # first player wins

state2 = ["..", "..", "..", ".."]  # second player wins

state3 = [".##.", "#..#", "#..#", ".##."]  # second player wins

state4 = [
    "#.......",
    ".....##.",
    ".....##.",
    "........",
    "........",
    "........",
    "........",
    "#......#",
]  # first


def solve(state):
    dp = {}

    # Returns list of list and whether at least a 2 x 2 squares remains.
    # The nested list can contains only tuple for a single sqaure, or 4 tuples for 2x2 squares
    def find_valid_moves(state):
        ans = []
        has_four_squares = False
        for r in range(len(state)):
            for c in range(len(state[0])):
                if state[r][c] == ".":
                    ans.append([(r, c)])
                if r != 0 or c == len(state[0]) - 1:
                    # Not valid positions for 2 x 2 squares starting from this position to their right
                    continue
                # First row and not the last colume
                if (
                    state[r][c] == "."
                    and state[r + 1][c] == "."
                    and state[r][c + 1] == "."
                    and state[r + 1][c + 1] == "."
                ):
                    has_four_squares = True
                    ans.append([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])
        return ans, has_four_squares

    # Given a state, recursion answers the question can you win?
    # For any valid moves, if in the substate any time returns a wins,
    # then we dont need to check anymore. In order for the second player
    # to win the state, for any valid moves of the first player, if there
    # exists a win for second player. Then it is a win.
    def recur(state):
        enc = str(state[0]) + str(state[1])
        if enc in dp:
            return dp[enc]
        valid_moves, has_four_squares = find_valid_moves(state)
        if len(valid_moves) == 0:
            return 0  # First player loses
        if len(valid_moves) == 1:  # Only one square is available
            return 1  # First player wins
        if len(valid_moves) == 5 and has_four_squares:
            return 1  # First player wins
        for move in valid_moves:
            clone_state = deepcopy(state)
            for r, c in move:  # Could be 1 sqaure or 2 x 2 squares
                clone_state[r][c] = "#"
            if (
                recur(clone_state) == 0
            ):  # If it is second player's turn, and all moves lead to loss; first player wins
                dp[enc] = 1
                return dp[enc]
        dp[enc] = 0
        return dp[enc]

    # Convert list of strings to 2d array
    arr = []
    for element in state:
        arr.append([c for c in element])

    nim_sum = 0
    for row_ix in range(0, len(arr) - 1, 2):
        result = recur(
            deepcopy([arr[row_ix], arr[row_ix + 1]])
        )  # XOR. Result = 1 means first player has a winning strategy for that subgame
        nim_sum ^= result

    if nim_sum == 0:
        return "second"
    return "first"


print(solve(state0))
print(solve(state1))
print(solve(state2))
print(solve(state3))
print(solve(state4))
