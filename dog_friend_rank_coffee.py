# Dog's friends have different taste of coffee and rank them differently.
# Given a list of list of strings representing each friend's coffee ranking (from high to low).
# For example [["Phils", "starbucks", "dunken donut"], ["starbucks", "mcdonald"]]
# Find out whether there exists a global ranking, if so, print it out. Otherwise,
# print out impossible. Recommended time complexity: O(nlogn) and space O(nlogn), where
# n = each coffee ranking item from a friend.

# coffee = [["Phils", "starbucks", "dunken"], ["starbucks", "mcdonald", "dunken"]]

# P -> star -> dunken
#        |down   | up
#        mcdonald

# ans = P -> star -> mc -> dunken
# respect local ranking, can you quickly find the item?

from collections import defaultdict


def topologicalSort(rankings):
    visited = set()
    stack = []
    adj = defaultdict(set)
    contain_cycle = False

    def topologicalSortUtils(parent):
        nonlocal contain_cycle

        # if parent in curr_visited:
        #     contain_cycle = True
        #     return
        if parent in visited:
            return
        curr_visited.add(parent)
        visited.add(parent)
        for child in adj[parent]:
            if child in curr_visited:
                contain_cycle = True
                continue
            if child not in visited:
                topologicalSortUtils(child)
        # When current visiting path ends, add the parent node to the visited set.
        curr_visited.remove(parent)
        # visited.add(parent)
        stack.append(parent)
        return

    for ranking in rankings:
        for ix in range(len(ranking)):
            if ix == len(ranking) - 1:
                if ranking[ix] not in adj:
                    adj[ranking[ix]] = set()
            else:
                adj[ranking[ix]].add(ranking[ix + 1])

    for item in adj:
        curr_visited = set()
        topologicalSortUtils(item)

    return stack[::-1] if not contain_cycle else "impossible"


# Correct answer: B A D C G F E
coffee = [
    ["B", "A", "C", "E"],  #
    ["B", "D", "G", "F"],  #
    ["A", "D", "G", "E"],  #
    ["D", "C", "F", "E"],  #
]

# coffee = [
#     ["Phils", "starbucks", "dunken"],
#     ["starbucks", "Phils", "mcdonald", "dunken"],
# ]

# coffee = [
#     ["Phils", "starbucks"],
#     ["starbucks", "Phils"],
# ]

print(topologicalSort(coffee))
