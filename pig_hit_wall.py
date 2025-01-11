grid = [  # Line 1
    ["9", ".", ".", "#"],
    # Line 2
    ["#", ".", ".", "."],  #
    # Line 3
    [".", ".", ".", "."],  #
    # Line 4
    ["1", ".", ".", "."],  #
]
# 9


# Idea: for every routes, keep track of the distance,
# As long as it is longer than the min distance, abort.
# So every step check against the min distance, do not
# repeat routes that you have visted.
def pig_hit_wall(grid):
    def is_position_valid(r, c):
        return (
            r >= 0
            and r < len(grid)
            and c >= 0
            and c < len(grid[0])
            and grid[r][c] != "#"
        )

    def dfs(r, c, direction, visited, curr_dist, min_dist):
        if not is_position_valid(r, c) or (r, c) in visited:
            return 1e6
        visited.add((r, c))
        # Early stop
        if curr_dist > min_dist:
            return 1e6
        if grid[r][c] == "9":
            return curr_dist
        # If keep moving the same direction makes sense (within bound and not #)
        if is_position_valid(r + direction[0], c + direction[1]):
            return dfs(
                r + direction[0],
                c + direction[1],
                direction,
                visited,
                curr_dist + 1,
                min_dist,
            )
        else:
            # Hit the boundary pixel
            curr_min_dist = min(
                dfs(r + 1, c, (1, 0), visited, curr_dist + 1, min_dist),
                dfs(r, c + 1, (0, 1), visited, curr_dist + 1, min_dist),
                dfs(r - 1, c, (-1, 0), visited, curr_dist + 1, min_dist),
                dfs(r, c - 1, (0, -1), visited, curr_dist + 1, min_dist),
            )
            if curr_min_dist < min_dist:
                min_dist = curr_min_dist
            return curr_min_dist

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                min_dist = min(
                    dfs(r, c, (1, 0), set(), 0, 1e6),
                    dfs(r, c, (0, 1), set(), 0, 1e6),
                    dfs(r, c, (-1, 0), set(), 0, 1e6),
                    dfs(r, c, (0, -1), set(), 0, 1e6),
                )
                if min_dist == 1e6:
                    return -1
                return min_dist


print(pig_hit_wall(grid))
