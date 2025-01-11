# Given a 2D plane of taylor swift's stamp points, pig can start from anywhere,
# but she only has certain amt of energy to travel, and she wants to visit
# as many unique swift's stamp point as possible. How many can she visit at most?
from copy import deepcopy

stamps = [
    [1, 0, 0, 3, 0],
    [0, 2, 0, 0, 4],
    [0, 0, 5, 0, 6],
    [0, 0, 0, 0, 0],
]

stamps = [
    [1, 2],  ###
    [3, 4],  ###
]

energy = 3


stamps = [
    [1, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 5],
]

energy = 20000

# DFS: start with any node and you can travel any notes. Implement early stopping.


def solve(stamps, energy):
    max_stamps = 0
    result = []

    def dfs(visited, node, total_stamps, left_energy):
        # nonlocal net # only need nonlocal for doing assignment
        nonlocal max_stamps
        nonlocal result
        visited.append(node)
        if total_stamps == len(net.keys()) or left_energy < 0:
            if max_stamps < total_stamps:
                result = visited
            max_stamps = max(max_stamps, total_stamps)
            return
        x1, y1 = net[node]
        for n_node in net.keys():
            if n_node == node:
                continue
            x2, y2 = net[n_node]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if n_node not in visited:
                dfs(
                    deepcopy(visited), n_node, total_stamps + 1, left_energy - dist
                )  # Remember visited cannot be shared between recursive calls
        visited.pop()  # Remove the last node when all the nn have been processed.

    net = {}
    for r in range(len(stamps)):
        for c in range(len(stamps[0])):
            node = stamps[r][c]
            if node != 0:
                net[node] = (r, c)

    for node in net.keys():
        visited = []
        dfs(visited, node, 1, energy)
    return max_stamps, result


print(solve(stamps, energy))
