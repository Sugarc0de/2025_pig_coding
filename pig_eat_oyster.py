from pprint import pprint

grid = [
    # Line 1
    [1, 1, 1, 2],  #
    # Line 2
    [1, 1, 1, 1],  #
    # Line 3
    [1, 1, 1, 1],  #
    # Line 4
    [2, 1, 1, 1],  #
]  # ans = 9


# This is a DP problem. The DP structure should be a 2d grid: DP[r,c] represents the max side of a square using the current coord as the right bottom coords
# of the square.
def pig_eat_oyster(grid):
    dp = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r == 0 or c == 0:
                continue
            elif (
                len(
                    set(
                        [grid[r - 1][c], grid[r - 1][c - 1], grid[r][c - 1], grid[r][c]]
                    )
                )
                == 1
            ):
                dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1
    ans = 0
    for r in range(len(dp)):
        for c in range(len(dp[0])):
            if dp[r][c] > ans:
                ans = dp[r][c]
    return ans**2


# Simple variation: just find the max number of the connected pieces with the same values
def pig_eat_oyster_non_square(grid):
    visited = set()
    max_cell = 0

    def find_neighbors(r, c):
        result = []
        if c + 1 < len(grid[0]) and r + 1 < len(grid):
            result.append((r + 1, c + 1))
        if c + 1 < len(grid[0]):
            result.append((r, c + 1))
        if r + 1 < len(grid):
            result.append((r + 1, c))
        return result

    def dfs(r, c):
        curr_max_cell = 0
        neighbors = find_neighbors(r, c)
        for nr, nc in neighbors:
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            if grid[nr][nc] == grid[r][c]:
                curr_max_cell += 1 + dfs(nr, nc)
        return curr_max_cell

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in visited:
                continue
            curr_max_cell = 1 + dfs(r, c)
            if curr_max_cell > max_cell:
                max_cell = curr_max_cell
    return max_cell


# print(pig_eat_oyster_non_square(grid))  # 12
print(pig_eat_oyster(grid))  # 9
