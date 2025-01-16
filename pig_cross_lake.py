# Given the polygonal shape lake with all the vertices,
# find whether a polygon is convex in O(n) runtime, where
# n is the number of vertices. The polygon is not self-
# intersecting. Convex means any vertex can be connected
# to any other vertex with the line inside the polygon.
# All the points are given in order. The lake will not have
# three points on the same line.

import numpy as np

vs1 = [[4, 8], [8, 8], [10, 6], [8, 2], [4, 4], [4, 8]]
# ans = True

vs2 = [[2, 4], [5, 4], [4, 3], [5, 2], [3, 2], [2, 4]]
# ans = False

# Idea: for all the points, if they all have the same orientation, then it is convex. Otherwise not.


def check_orientation(p1, p2, p3):
    # Form two vectors, p2p1 and p2p3 and find the cross product
    p1x, p1y = p1
    p2x, p2y = p2
    p3x, p3y = p3
    p2p1 = np.array([p1x - p2x, p1y - p2y])
    p2p3 = np.array([p3x - p2x, p3y - p2y])
    cross_product = np.cross(p2p1, p2p3)
    return 1 if cross_product > 0 else -1


def solve(vertices):
    orientation = None
    vertices.append(
        vertices[1]
    )  # Concatenate the second item to the end of the vertices list
    for ix in range(1, len(vertices) - 1):
        p1 = vertices[ix - 1]
        p2 = vertices[ix]
        p3 = vertices[ix + 1]
        curr_orientation = check_orientation(p1, p2, p3)
        if orientation is None:
            orientation = curr_orientation
        elif orientation != curr_orientation:
            return False
    return True


print(solve(vs1))
print(solve(vs2))

vs_test = [[0.1, 0.1], [1, 0], [0, 0], [0, 1], [0.1, 0.1]]
print(solve(vs_test))
