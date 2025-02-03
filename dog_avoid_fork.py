# SPEED CHALLENGE. Given all the positions on the chess board from (1, 1) to (8, 8).
# Find all the positins that a fork can happen so dog can avoid.


def dog_gets_forked(pos):
    # Return all the forked positins for current pt
    def find_fork_pos(pt):
        x, y = pt
        ans = set()
        offset = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]
        for dx, dy in offset:
            nx = x + dx
            ny = y + dy
            if nx < 1 or nx > 8 or ny < 1 or ny > 8:
                continue
            if (nx, ny) in pos:
                continue
            ans.add((nx, ny))
        return ans

    visited = set()
    forked = set()
    for pt in pos:
        pt_forked = find_fork_pos(pt)
        # print("pt forked is: ", pt_forked)
        for candidate in list(pt_forked):
            if candidate not in visited:
                visited.add(candidate)
            else:
                # print("visited: ", visited)
                forked.add(candidate)

    return list(forked)


print(dog_gets_forked([(2, 5), (3, 7), (4, 4), (6, 4)]))  # = [(4, 5), (5, 2), (5, 6)]
print(dog_gets_forked([(5, 5), (5, 6), (6, 6)]))
