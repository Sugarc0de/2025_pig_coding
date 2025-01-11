# Given a 2D plane, pig is at home (0, 0), facing north. everytime she can turn left or right
# with a float representing the angle in degree [0, 180], then walk forward for m mins (m is a float),
# Find the way home in one step, eg: turn right and then walk 15 mins to home.
import math
import numpy as np

input1 = [  # Line 1
    ("left", 45, 2**0.5),  #
    ("right", 45, 1),
    # Line 2
    # ("left", 45, 10),
]  # direction, anlge, mins to walk


# When you calculate the angle from left or right, always convert it in terms of 0 (east), 90 (north), 180 (west), and 270 (south) degree.
def solve(input):
    _, _, distance = input[0]
    location_vector = [0, 0]
    direction_vector = [0, 1]
    for turn, angle, distance in input:
        if turn == "left":
            sin_theta = math.sin(math.radians(angle))
            cos_theta = math.cos(math.radians(angle))
            print("Angle: ", angle)
        elif turn == "right":
            sin_theta = math.sin(math.radians(-angle))
            cos_theta = math.cos(math.radians(-angle))
            print("Angle: ", -angle)
        print("sin theta: ", sin_theta)
        print("cos theta: ", cos_theta)
        Rot_mat = np.array(
            [[cos_theta, -sin_theta], [sin_theta, cos_theta]]
        )  # counter clockwise is positive
        print("R mat: ", Rot_mat)
        print("prev direction vector: ", direction_vector)
        direction_vector = np.matmul(Rot_mat, direction_vector)
        print("curr direction vector: ", direction_vector)
        scaled_vector = distance * direction_vector
        print("scale vector: ", scaled_vector)
        location_vector = location_vector + scaled_vector
        print("location vector: ", location_vector)
        print("****************************************")
    # Need to find the angle between the dirction vector and the location vector
    # But you need to reverse the location vector to be a vector that points to home

    home_vector = -location_vector

    # Calculate angles
    home_theta = math.degrees(
        math.atan2(home_vector[1], home_vector[0])
    )  # returns between -180 and 180
    dir_theta = math.degrees(math.atan2(direction_vector[1], direction_vector[0]))

    # Find angle difference which might exceed -180 so wrap to [-180, 180]
    angle = home_theta - dir_theta

    angle = (
        angle + 180
    ) % 360 - 180  # (angle + 180) % 360 brings to the (0, 360) range

    # Determine turn direction
    turn = "left" if angle > 0 else "right"

    # Calculate distance to home
    distance = np.linalg.norm(location_vector)

    return (turn, abs(angle), distance)


print(solve(input1))
