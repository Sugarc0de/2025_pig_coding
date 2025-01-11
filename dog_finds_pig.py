# Dog tries to find pig in the skiing passes. He does not know where pig is and tries to find pig by visiting all the edges.
# Pig is on one of the edges. But dog does not want to visit the same edge more than twice, and it must includes going back
# to where he starts. Find one of the routes or else print out impossible. The graph is connected and dog can visit any vertex
# multiple times.
from collections import defaultdict


def solve(vertices):
    visited_edges = defaultdict(int)
    visited_vertices = set()
    adj = defaultdict(set)
    for v1, v2 in vertices:
        adj[v1].add(v2)
        adj[v2].add(v1)
    routes = []
    v1, _ = vertices[0]
    visited_vertices.add(v1)

    def dfs(v1):
        # Base case: no more unvisited vertex, have to traverse back
        for v2 in adj[v1]:
            edge = tuple(sorted([v1, v2]))
            if edge not in visited_edges:
                # The other vertex has been visited, so go there and back immediately
                if v2 in visited_vertices:
                    visited_edges[edge] += 1
                    routes.append((v1, v2))
                    routes.append((v2, v1))
                # Has not visited the other vertex
                elif v2 not in visited_vertices:
                    visited_edges[edge] += 1
                    visited_vertices.add(v2)
                    routes.append((v1, v2))
                    dfs(v2)
                    routes.append((v2, v1))

    dfs(v1)
    return routes


vertices = [[1, 2], [2, 3], [2, 4], [2, 5], [4, 5], [4, 1], [5, 1]]
print(solve(vertices))
