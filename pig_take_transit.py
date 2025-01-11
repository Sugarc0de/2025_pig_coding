from collections import defaultdict, deque


# Github solution below


# Helper function
def construct_graph(routes):
    G = defaultdict(set)
    for name in routes:
        for ix, stop_name in enumerate(routes[name]):
            G[stop_name] = G[stop_name].union(set(routes[name][ix + 1 :]))
    return G


# Method: BFS
def find_least_transit(routes_map, start, end):
    G = construct_graph(routes_map)
    print("Graph is ", G)
    Q = deque()
    visited = set()
    Q.append((start, 0))
    visited.add(start)
    while len(Q) > 0:
        stop, steps = Q.popleft()
        if stop == end:
            return steps
        for next_stop in G[stop]:
            if next_stop not in visited:
                visited.add(next_stop)
                Q.append((next_stop, steps + 1))
    return -1


##########################################################################################################


# Bonus: what if you wanna print out the route names?
def pig_take_transit(routes, start, end):
    stops = defaultdict(list)
    for key in routes.keys():
        # (route_name, stop #, distance) assume the distance between any stops on the same route is 1
        for prev_ix in range(len(routes[key]) - 1):
            for next_ix in range(prev_ix + 1, len(routes[key])):
                stops[routes[key][prev_ix]].append((key, routes[key][next_ix], 1))
    stack = deque()
    visited = set()
    min_dist = -1
    # BFS
    for values in stops[start]:
        stack.append(values)
    visited.add(start)
    while len(stack):
        (curr_route, curr_stop, curr_dist) = stack.popleft()
        if curr_stop == end:
            return curr_dist
        if curr_stop in visited:
            continue  # Avoid a loop
        for next_route, next_stop, next_dist in stops[curr_stop]:
            stack.append((next_route, next_stop, next_dist + curr_dist))
        visited.add(curr_stop)
    return min_dist


routes1 = {
    # Line 1
    "yonge": ["A", "B", "O", "D", "F"],
    # Line 2
    "bay": ["C", "D", "L", "Y", "K"],
    # Line 3
    "dundas": ["I", "O", "K", "G"],
    # Line 4
    "king": ["K", "F", "G", "N"],
}

start1 = "A"
end1 = "K"
print(find_least_transit(routes1, start1, end1))  # 2

start1 = "A"
end1 = "C"
print(find_least_transit(routes1, start1, end1))  # -1

routes2 = {
    # Line 1
    "yonge": ["A", "B", "C", "D", "E"],
    # Line 2
    "bay": ["A", "E", "F", "G", "H"],
    # Line 3
    "dundas": ["I", "O", "K", "G"],
    # Line 4
    "king": ["K", "F", "G", "N"],
}

start2 = "A"
end2 = "H"

print(find_least_transit(routes2, start2, end2))  # 1

inf_routes = {
    # Line 1
    "yonge": ["A", "B"],
    # Line 2
    "yonge_reverse": ["B", "A"],
    # Line 3
    "dundas": ["C", "O", "K", "G"],
    # Line 4
    "king": ["K", "F", "G", "N"],
}

start3 = "A"
end3 = "K"

print(find_least_transit(inf_routes, start3, end3))
