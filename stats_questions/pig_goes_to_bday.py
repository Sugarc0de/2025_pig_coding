# Category: Probability (difficulty: 4)
#
# Today is day 0 and is pig's bday. Pig has n friends, each
# one of their bday is uniformly random, assuming 365 days
# a year. Let d be the number of days until next friend's bday
# party. Compute the pdf for all d where d >= 0 and d < 366.
# Return a list of 365 length where idx is pdf for d.


import numpy as np


def solve(n):
    s = np.random.uniform(0, 355, n)
