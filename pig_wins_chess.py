# Pig has a winning rate of pw (0 <= pw <= 1), drawing rate pd, pw + pd + q = 1. she and dog play t games, find the probability that
# she gets at least s points. Assuming a win gets 1 points, drawing gets 0.5 point.


# DP: [i, j] where i represents the total number of games dog play, j means the number of points he gets. DP[i,j] stores the probability
# of getting to this number of points at game i. For example, if total number of game is 20 (max 20 points), and pig needs to get at least 12 points.
# it means 1 - (dog[20, 0] + dog[20, 0.5] + dog[20, 1] + dog[20, 2] + ... dog[20, 8])

from scipy.stats import norm
from math import sqrt
import numpy as np
from pprint import pprint


# def calculate_win_prob(pig_pw, pd, t, s):
#     pig_pl = 1 - pig_pw - pd
#     dog_pw = pig_pl
#     dog_pl = pig_pw
#     dp = {}
#     dp[(1, 1)] = dog_pw
#     dp[(1, 0.5)] = pd
#     dp[(1, 0)] = dog_pl
#     for i in range(
#         2, t + 1
#     ):  # total game played -- starting from 2 games cuz 1 is already covered by the base case.
#         for j in np.arange(0, t - s + 1, 0.5):
#             if j > i:  # impossible position, score > total game played
#                 continue
#             if j == 0:
#                 # dog has not win
#                 dp[(i, j)] += dp[(i - 1, j)] * dog_pl
#             if j == 0.5:
#                 # dog has only one draw
#                 dp[(i, j)] = dp[(i - 1, j)] * dog_pl + dp[(i - 1, j - 0.5)] * pd
#                 continue
#             else:
#                 dp[(i, j)] = (
#                     dp[(i - 1, j)] * dog_pl
#                     + dp[(i - 1, j - 1)] * dog_pw
#                     + dp[(i - 1, j - 0.5)] * pd
#                 )
#     dog_wins = 0
#     for j in np.arange(0, t - s + 1, 0.5):
#         dog_wins += dp[t][j]

#     return 1 - dog_wins


def calculate_win_prob(pw, pd, total_games, min_scores):
    dp = {}

    def recur(pw, pd, t, s):
        if s > t:
            return 0  # Dont need to add the invalid position to dp map
        pl = 1 - pw - pd
        if (t, s) in dp:
            return dp[(t, s)]
        if t == 1:
            if s == 0:
                dp[(t, s)] = pl
            if s == 0.5:
                dp[(t, s)] = pd
            if s == 1:
                dp[(t, s)] = pw
        elif s == 0:
            dp[(t, s)] = recur(pw, pd, t - 1, s) * pl
        elif s == 0.5:
            dp[(t, s)] = recur(pw, pd, t - 1, s - 0.5) * pd
        else:
            dp[(t, s)] = (
                recur(pw, pd, t - 1, s) * pl
                + recur(pw, pd, t - 1, s - 1) * pw
                + recur(pw, pd, t - 1, s - 0.5) * pd
            )
        return dp[(t, s)]

    recur(pw, pd, total_games, min_scores)
    # Pig needs to win at least s points
    win_prob = 0
    pprint(dp)
    for score in np.arange(min_scores, total_games + 1, 0.5):
        if (total_games, score) in dp:
            win_prob += dp[(total_games, score)]
    return win_prob


# How to verify the correctness. Approximation assume the number of games is large, use central limit theorem:
# Xi represent the the number of points earned in a single game. Xi can be 0, 0.5, or 1. P = sum of Xi represent
# the total points you get in all game. E(Xi) = pw * 1 + pd * 0.5. var(Xi) = E(Xi^2) - E(Xi)^2
# = (1^2 * pw + 0.5^2 * pd) - (pw + 0.5pd)^2. P follows a normal distribution with mean = N*(E(Xi)) and var = N * var(Xi)
# Now assumes p(X) means total points dog get


def approximate(pw, pd, t, s):  # t is total game, s is number of points pig has to get
    mean = t * (pw + pd * 0.5)
    var = t * ((pw + (0.5**2) * pd) - ((pw + 0.5 * pd) ** 2))
    std = sqrt(var)
    # pig at least wins s points = 1 - CDF(X <= s)
    return 1 - norm.cdf(
        s, loc=mean, scale=std
    )  # cdf(x) Calculate the cumulative probability for X <= x


# should be 1
print(calculate_win_prob(0.5, 0.3, 2, 0))

# should be 0.84
# WW 0.25 WD 0.15 WL 0.1 DW 0.15 DD 0.09 LW 0.1
print(calculate_win_prob(0.5, 0.3, 2, 1))

# should be 0.25
print(calculate_win_prob(0.5, 0.3, 2, 2))


# print(calculate_win_prob(0.6, 0.2, 1, 1))
# print(approximate(0.6, 0.2, 1, 1))
# print("***************************************")

# print(calculate_win_prob(0.4, 0.2, 2, 0))
# print(approximate(0.4, 0.2, 2, 0))
# print("***************************************")

# print(calculate_win_prob(0.4, 0.2, 2, 1))
# print(approximate(0.4, 0.2, 2, 1))
# print("***************************************")

# print(calculate_win_prob(0.4, 0.2, 3, 2))
# print(approximate(0.4, 0.2, 3, 2))
# print("***************************************")

# print(calculate_win_prob(0.5, 0, 99, 50))
# print(approximate(0.5, 0, 99, 50))
# print("***************************************")

# print(calculate_win_prob(0.4, 0.2, 99, 30))
# print(approximate(0.4, 0.2, 99, 30))
# print("***************************************")

# print(calculate_win_prob(0.4, 0.2, 1001, 100))
# print(approximate(0.4, 0.2, 1001, 100))

# print("***************************************")

# print(calculate_win_prob(0.1, 0.2, 1000, 100))
# print(approximate(0.1, 0.2, 1000, 200))
# print("***************************************")
