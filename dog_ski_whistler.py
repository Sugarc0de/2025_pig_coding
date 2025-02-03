# Dog is trying to ski down from Whistler, but he is slightly afraid of height so he can ski maximum 10 degree down.
# Given a 2D surface as a function, we have dog's location as (x, y) and the function will produce z. Find the directional
# vector that points towards 10 degree. Return the degree if less than 10 is maximum.

# Assume the mountain is -0.2x^2 - 0.4y^2 + 0.8x - 0.5y + 1000
# Difficulty: 6

import math

# x = 1, y = 2
# gradient is [ 0.4, -2.1 ]
# answer: angle to ski at 10 degrees: [-0.994, -0.105] as directional vector


def rotate(x, y, deg):
    rad = -math.radians(deg)
    return (
        math.cos(rad) * x + math.sin(rad) * y,
        -math.sin(rad) * x + math.cos(rad) * y,
    )


def solve(x, y, desired_slope):

    grad_x = lambda x: -0.4 * x + 0.8
    grad_y = lambda y: -0.8 * y - 0.5
    dzdx = grad_x(x)
    dzdy = grad_y(y)
    print("dzdx: ", dzdx)
    print("dzdy: ", dzdy)
    # Check the gradient (maximum angle) to see if it is greater than 10
    # directional vector is at the same direction as gradient
    theta = math.degrees(math.atan(math.sqrt(dzdx**2 + dzdy**2)))
    print("theta: ", theta)
    if theta <= desired_slope:
        return theta

    magnitude_grad = (dzdx**2 + dzdy**2) ** 0.5
    norm_grad_x = -dzdx / magnitude_grad
    norm_grad_y = -dzdy / magnitude_grad

    # find alpha such that the slope is less than 10 using binary search.
    lo = 0
    hi = 90
    while hi - lo > 0.000001:
        mid = (lo + hi) / 2
        # Find the first alpha lo such that its directional vector (which way to ski) has slope <= 10
        print(lo, mid, hi)
        # print("cos of mid: ", math.cos(mid))
        # print("sin of mid: ", math.sin(mid))

        # direction is take norm([gradx, grady]) and rotate right by mid degrees
        direction_x, direction_y = rotate(norm_grad_x, norm_grad_y, mid)
        slope = abs(direction_x * dzdx + direction_y * dzdy)
        theta = math.degrees(math.atan(slope))
        if theta <= desired_slope:
            hi = mid
        else:
            lo = mid

        # slope = abs(
        #     math.cos(math.radians(mid)) * dzdx + math.sin(math.radians(mid)) * dzdy
        # )
        # print("slope: ", slope)
        # if slope <= math.tan(math.radians(desired_slope)):
        #     lo = mid
        # else:
        #     hi = mid
    return direction_x, direction_y


print(solve(0, -2, 30))
