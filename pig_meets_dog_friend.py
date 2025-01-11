# Dog has a lot of friends, and everyone knows dog and at least one other friend.
# Given this connection network, e.g, a list of tuples of friends'name who know
# each other. Dog wants to randomly select n friends to meet together (2 <= n <= 4),
# what is the probability that this n people all know each other?
from collections import defaultdict


def solve(friends, n):
    cliques = []
    adjacency = defaultdict(set)
    for persons in friends:
        for person in persons:
            adjacency[person].update(list(persons))
            adjacency[person].remove(person)
    # print("adjacency graph: ", adjacency)

    # friend in friend cycle should all know each other
    def backtrack(friend_circle, n):
        if friend_circle in cliques:
            return
        if len(friend_circle) == n:
            cliques.append(friend_circle)
            return

        friend_circle = list(friend_circle)
        ix = 0
        while ix < len(friend_circle):
            friend = friend_circle[ix]
            for new_friend in adjacency[friend]:
                if new_friend == friend or new_friend in friend_circle:
                    continue
                # check if new_friend is also in friend_cycle.
                other_friend_cycle = friend_circle[:ix] + friend_circle[ix + 1 :]
                should_add_new_friend = True
                for other_friend in other_friend_cycle:
                    if new_friend not in adjacency[other_friend]:
                        should_add_new_friend = False
                        break
                if should_add_new_friend:
                    friend_circle_copy = set(friend_circle)
                    friend_circle_copy.add(new_friend)
                    backtrack(friend_circle_copy, n)
            ix += 1

    for person in adjacency:
        init_friend_cycle = set()
        init_friend_cycle.add(person)
        backtrack(init_friend_cycle, n)
    return cliques


friends = [
    ("A", "B"),
    ("A", "C"),
    ("A", "D"),
    ("D", "C"),
    ("D", "B"),
    ("B", "C"),
    ("B", "E"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F"),
    ("G", "F"),
]
print(solve(friends, 4))
