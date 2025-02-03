# Pig tries to find free coffee in the forestry building. Assume there are m floors, and each floor has
# at least 2 coffee spots. Pig starts from the top floor and can travel left and right and down but can
# never travel back up. Find out the best route with minimum travel distance to visit all the coffee
# places. Difficulty: 6, string DP.

map = [
    "c....c",  #
    ".c.c.c",  #
    "c...c.",  #
    "..cc..",  #
    "c....c",  #
]

# Idea: we only care about the far left and far right coffee location for each floor. And we need
# to just track whether the lowest distance to visit the current coffee comes from the far left or
# far right position of the coffee on the upper floor. So DP[i, j] where j = 0 and 1, keeps track of
# the minimum distance to reach the i floor left (j=0) or right (j=1) coffee, provided that it has
# already reached other coffee on the same row and above.


def solve(map):
    dp = [[None] * 2 for _ in range(len(map))]
    print("dp: ", dp)
    indices = []
    for i in range(len(map)):  # Start from idx 0 (top floor)
        left_coffee = 0
        right_coffee = len(map[0]) - 1
        for j in range(len(map[0])):
            if map[i][j] == "c":
                left_coffee = j
                break
        for j in range(len(map[0]) - 1, -1, -1):
            if map[i][j] == "c":
                right_coffee = j
                break

        indices.append((left_coffee, right_coffee))
    print("indices: ", indices)

    # 0 if we came from the left, 1 if from the right of the previous row
    came_from_right = [[None] * 2 for _ in range(len(map))]

    def recur(i, j):  # j is 0 or 1
        if dp[i][j] is not None:
            return dp[i][j]
        h_dist = (
            indices[i][1] - indices[i][0]
        )  # distance to another coffee on the other side
        if i == 0:  # base case
            dp[i][j] = h_dist
            return dp[i][j]

        recur(i - 1, 0)
        recur(i - 1, 1)

        left_case_ix = indices[i - 1][0]
        right_case_ix = indices[i - 1][1]

        if j == 0:
            # From the left coffee in the prev row, go down, then to the right on this row, then to the left
            left_path = dp[i - 1][0] + 1 + abs(left_case_ix - indices[i][1]) + h_dist

            # From the right coffee in the prev row, go down, then to the right on this row, then to the left
            right_path = dp[i - 1][1] + 1 + abs(right_case_ix - indices[i][1]) + h_dist

        else:
            # From the left coffee in the prev row, go down, then to the left on this row, then to the right
            left_path = dp[i - 1][0] + 1 + abs(left_case_ix - indices[i][0]) + h_dist

            # From the right coffee in the prev row, go down, then to the left on this row, then to the right
            right_path = dp[i - 1][1] + 1 + abs(right_case_ix - indices[i][0]) + h_dist

        ans = min(left_path, right_path)
        if ans == left_path:
            came_from_right[i][j] = False
        else:
            came_from_right[i][j] = True

        dp[i][j] = ans
        return ans

    for j in range(2):
        recur(len(map) - 1, j)

    print("came from: ", came_from_right)

    if dp[-1][0] < dp[-1][1]:
        ending_position = (len(map) - 1, indices[-1][0])
        is_right = False
    else:
        ending_position = (len(map) - 1, indices[-1][1])
        is_right = True

    # Return a list of coordinates to go from (r, a), to (r, b), then up to (r, c) and up to (r-1, c)
    # Inclusive of (r-1, c) but not including (r, a)
    # Eg: partial_path(4, 1, 5, 3)
    # (4, 2), (4, 3), (4, 4), (4, 5), (4, 4), (4, 3), (3, 3)
    def get_partial_path(r, a, b, c):
        partial_path = []
        j = a
        while j != b:
            if j < b:
                j += 1
            else:
                j -= 1
            partial_path.append((r, j))

        while j != c:
            if j < c:
                j += 1
            else:
                j -= 1
            partial_path.append((r, j))

        if r != 0:
            partial_path.append((r - 1, j))
        return partial_path

    path = [ending_position]
    for r in range(len(map) - 1, -1, -1):
        cur_pos = indices[r][1] if is_right else indices[r][0]
        other_pos = indices[r][0] if is_right else indices[r][1]
        if came_from_right[r][int(is_right)]:
            above_pos = indices[r - 1][1]
            is_right = True
        else:
            above_pos = indices[r - 1][0]
            is_right = False
        partial_path = get_partial_path(r, cur_pos, other_pos, above_pos)
        path.extend(partial_path)

    # def reconstruct():
    #     # Idea: start from the bottom floor, add the (x, y) with the minimum distance first
    #     # Then add its neighbor, check the came from to add the previous point, and then add
    #     # its neighbor. Stop when you reach to the top floor
    #     path = []
    #     i = len(dp) - 1
    #     if (
    #         dp[i][1] >= dp[i][0]
    #     ):  # First add the right, then add the left (in reversed order)
    #         path.append((i, indices[i][0]))
    #         path.append((i, indices[i][1]))
    #     else:
    #         path.append((i, indices[i][1]))
    #         path.append((i, indices[i][0]))
    #     prev_came_from =

    path = list(reversed(path))
    return path


print(solve(map))
