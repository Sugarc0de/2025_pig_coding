from collections import defaultdict

tree = [
    ("A", "B", 3),
    ("A", "C", 1),
    ("B", "D", 6),
    ("B", "E", 1),
    ("C", "F", 2),
    ("D", "G", 3),
    ("E", "H", 4),
    ("F", "I", 5),
]
target = 15


def dfs(tree, target):
    D = defaultdict(list)
    child_set = set()
    for parent, child, dist in tree:
        D[parent].append([child, dist])
        child_set.add(child)
    root = list(set(D.keys()).difference(child_set))[0]
    stack = []
    result = 0
    for child, dist in D[root]:
        stack.append([child, dist, target])
    while stack:
        node, dist, rem = stack.pop()
        curr_rem = rem - dist
        if curr_rem < 0:
            continue
        if not D[node]:
            # Already left node
            result += 1
        for child, dist2 in D[node]:
            stack.append([child, dist2, rem - dist])
    return result


print(dfs(tree, target))
