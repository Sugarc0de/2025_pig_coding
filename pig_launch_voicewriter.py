# Pig needs to predict user growth for voice writer. Dog is confident that it is a quadratic
# distribution of ax^2 + bx + c form and the launch day user must be at the vertex. Fit the best
# parabola and plot it out. The quadratic curve must go upward, if impossible, just plot a flat curve.

import numpy as np
from scipy.linalg import lstsq

user_data = [[2, 10], [5, 12], [8, 18], [6, 12]]  # day, the number of users


def solve(user_data):
    x_min, y_min = user_data[0]
    M = []
    b = []
    for x, y in user_data[1:]:
        M.append([(x - x_min) ** 2])
        b.append([y - y_min])
    M = np.array(M)
    b = np.array(b)

    x, residuals, rank, s = lstsq(M, b)

    print("Solution:", x)
    print(f"Function form: {x[0][0]}*(x-{x_min})**2 + {y_min}")


print(solve(user_data))
