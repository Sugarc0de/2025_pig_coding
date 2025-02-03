# Pig and dog wants to choose a neighborhood. Dog has a criteria that dog wants to see pig whenever they walk separately.
# Neighborhood is a quadratic polynomial f(x, y) = Ax^2 + By^2 + Cxy + Dx + Ey + F and you are given [A, B, C, D, E, F]
# as input. Determine if a given neighborhood is suitable.

# Difficulty: 4. Requires Hessian matrix and eigenvectors
import numpy as np
from numpy import linalg


def solve(A, B, C, D, E, F):
    fxx = 2 * A
    fxy = C
    fyx = C
    fyy = 2 * B
    hessian = np.array([[fxx, fyx], [fxy, fyy]])
    eig_values = linalg.eigvals(hessian)
    # print(hessian)
    # print(eig_values)

    # positive = None
    # negative = None
    # for ei in eig_values:
    #     if ei > 0:
    #         positive = True
    #     if ei < 0:
    #         negative = True
    #     if positive == True and negative == True:
    #         return "Not suitable"
    # if positive:
    #     # Convex
    #     return "Suitable"
    # return "Not suitable"

    for ei in eig_values:
        if ei < -1e-6:
            return False
    return True


print(solve(A=4, B=-3, C=12, D=-4, E=1, F=-11))  # Not suitable

print(solve(A=4, B=-1, C=1, D=-3, E=0, F=0))  # Not Suitable

# Suitable
print(solve(A=0, B=0, C=0, D=0, E=0, F=0))
print(solve(A=0, B=0, C=0, D=3, E=2, F=5))
print(solve(A=2, B=0, C=0, D=3, E=2, F=5))

# Not suitable
print(solve(A=2, B=-1, C=0, D=3, E=2, F=5))
print(solve(A=0, B=-1, C=0, D=3, E=2, F=5))

# Not suitable
print(solve(A=2, B=1, C=3, D=3, E=2, F=5))
print(solve(A=2, B=1, C=-3, D=3, E=2, F=5))
# Suitable
print(solve(A=2, B=1, C=2, D=3, E=2, F=5))
print(solve(A=2, B=1, C=-2, D=3, E=2, F=5))
