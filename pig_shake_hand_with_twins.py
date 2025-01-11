# Pig's location (x, y). A sa and A guil both starts at (0, 0) and they choose a direction (float number)
# between 0 and 360 uniformly. They then walk towards that direction. Calculate the probability that pig
# can shake hands with any of them at least once (Pig can shake hands if they are within 1 m apart)
import math


def solve(cx, cy):
    # Find we need to find the angle between two lines and the circle
    # Then use that angle / 360 to represent the probability of one twin
    # that can shake hands with pig. At least once means that we can have
    # 1 - P(no hand shake)
    between_point_distance = math.sqrt(cx**2 + cy**2)
    if between_point_distance <= 1:
        return 1
    print("between distance: ", between_point_distance)
    angle = math.degrees(math.asin(1 / between_point_distance)) * 2
    print("angle: ", angle)
    prob_not_to_meet = (360 - angle) / 360
    print("probability not to meet: ", prob_not_to_meet)
    return 1 - prob_not_to_meet * prob_not_to_meet


input1 = (2, 2)
print(solve(*input1))

print("*********************************")

input2 = (5, 10)
print(solve(*input2))

print("*********************************")

input3 = (-3, -9)
print(solve(*input3))

print("*********************************")

input4 = (-3, 3)
print(solve(*input4))


print("*********************************")

input5 = (-1.4142, 0)
print(solve(*input5))

print("*********************************")
