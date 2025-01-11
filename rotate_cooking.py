# Should use DP to solve this.

# Example:
days = 2
d_max = 1  # max days dog would cook
t_max = 1  # max days they would order takeout

# ans:
# [P, P], [P, D], [D, P], [P, T], [T, P], [D, T], [T, D]


def rotate_cooking(day, d_max, t_max):
    if day == 0:
        return 0
    if day == 1:
        return 1 + d_max + t_max
    combination = 1  # default is pig
    if d_max > 0:
        combination += 1 + rotate_cooking(day - 1, d_max - 1, t_max)
    if t_max > 0:
        combination += 1 + rotate_cooking(day - 1, d_max, t_max - 1)
    return combination


print(rotate_cooking(days, d_max, t_max))
