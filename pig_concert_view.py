# Given (x, y) as pig's location, Billie Eilish is at (0, 0), and each
# stero is a unit square, given the coordinates of the center, can be
# two float, the stero should align with the x axis. Guarantee that pig
# is not on the x and y axis. Guarantee that pig is not inside the stero.
# Stero should not be overlapping.

# Idea: How is Orientation useful here?
# Two segments (p1,q1) and (p2,q2) intersect if and only if one of the following two conditions is verified

# 1. General Case:
# – (p1, q1, p2) and (p1, q1, q2) have different orientations and
# – (p2, q2, p1) and (p2, q2, q1) have different orientations.

# Dont need to care about the collinearity
import numpy as np


EPS = 0.000000001


# Given all the legit vertices pair forming a line segment given center of unit square
def find_vertice_pairs(x, y):
    half_unit = 0.5
    left_bottom_vertex = (x - half_unit, y - half_unit)
    left_top_vertex = (x - half_unit, y + half_unit)
    right_bottom_vertex = (x + half_unit, y - half_unit)
    right_top_vertex = (x + half_unit, y + half_unit)
    return [
        [left_bottom_vertex, left_top_vertex],
        [left_top_vertex, right_top_vertex],
        [right_top_vertex, right_bottom_vertex],
        [left_bottom_vertex, right_bottom_vertex],
        # [left_bottom_vertex, right_top_vertex],
        # [left_top_vertex, right_bottom_vertex],
    ]


# return z scalar from the cross product of (p1, q1) to (p2, q2) to (p3, q3)
def check_orientation(p1, q1, p2, q2, p3, q3):
    # Slope between the first two point
    # first_slope = (q2 - q1) / (p2 - p1)
    # # Slope between second point and third point
    # second_slope = (q3 - q2) / (p3 - p2)

    # Use cross product instead
    first_vertex = np.array([p1, q1, 0])
    second_vertex = np.array([p2, q2, 0])
    third_vertex = np.array([p3, q3, 0])
    first_vector = second_vertex - first_vertex
    second_vector = third_vertex - second_vertex

    orientation = np.cross(first_vector, second_vector)
    return orientation[2]  # z component representing the orientation


# Pig: (x, y) location, stero locations is a list of tuples
def solve(pig_x, pig_y, stero_locations):
    origin_x = 0
    origin_y = 0
    for stero_x, stero_y in stero_locations:
        vertice_pairs = find_vertice_pairs(stero_x, stero_y)
        for vertice_pair in vertice_pairs:
            first_x, first_y = vertice_pair[0]
            second_x, second_y = vertice_pair[1]
            orientation1 = check_orientation(
                pig_x, pig_y, origin_x, origin_y, first_x, first_y
            )
            orientation2 = check_orientation(
                pig_x, pig_y, origin_x, origin_y, second_x, second_y
            )
            orientation3 = check_orientation(
                first_x, first_y, second_x, second_y, pig_x, pig_y
            )
            orientation4 = check_orientation(
                first_x, first_y, second_x, second_y, origin_x, origin_y
            )
            if (
                orientation1 * orientation2 < EPS and orientation3 * orientation4 < EPS
            ):  # want to check <= 0 but because of floating point issue, cant get exactly 0 reliably; use epsolon instead.
                return "intersected"

    return "not intersected"


# intersect
print(solve(4, 1, [(2.5, 0.5)]))

# intersect
print(solve(10, 2, [(2.5, 0.5)]))

# not intersect
print(solve(9, 5, [(2.5, 0.5)]))

# no
print(solve(9, 5, [(-1.5, -1.5)]))

# yes
print(solve(-3, -3, [(-1.5, -1.5)]))

# yes
print(solve(-4, -7, [(-1.5, -1.5)]))

# no
print(solve(-3, -1, [(-1.5, -1.5)]))

# no
print(solve(-0.5, -0.5, [(-1.5, -1.5)]))


# Test Case 1: stero is behind pig
# print(solve(1, 1, [(2, 2)]))

# Test Case 2: Pig near a stero, intersecting
# print(solve(2, 2, [(1, 1)]))

# Test Case 3: Pig between steros, not intersecting
# print(solve(1.5, 1.5, [(1, 1), (2, 2)]))

# # Test Case 4: Steros near the coordinate system corners
# print(solve(0.5, 0.5, [(-1, -1), (1, 1), (-1, 1), (1, -1)]))

# # Test Case 5: Multiple steros in different quadrants
# print(solve(-2, -3, [(-1, -1), (1, 1), (-2, 2), (2, -2)]))

# # Test Case 6: Steros touching at vertices
# print(solve(3, 3, [(1.5, 1.5), (2.5, 1.5)]))

# # Test Case 7: Pig on an extended line of a stero
# print(solve(3, 3, [(2.5, 2.5)]))

# # Test Case 8: Pig far away from steros
# print(solve(100, 100, [(-1, 1), (-2, -2)]))
