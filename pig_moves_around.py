# Pig's friend moves around, given a probabily that a person has certain probability to move from one given city to another.
# Calculate after a long period of time, find the distribution of pig's friends. What percentage of pig's friends is in each
# city.

import numpy as np
from scipy import linalg

prob = {
    "yvr": [("sea", 0.6), ("sfo", 0.4)],
    "sea": [("sfo", 0.3)],
    "sfo": [("sea", 0.1)],
}

# yvr, sea, sfo
transition_matrix = np.array(
    [  # line 1
        [0, 0.6, 0.4],
        # line 2
        [0, 0.7, 0.3],
        # line 3
        [0, 0.2, 0.8],
    ]
)


# Part A: assume there exist a limiting distribution
def compute_markov_chain(transition_matrix):
    b = np.identity(transition_matrix.shape[0])
    w, v = linalg.eig(transition_matrix, b, left=True, right=False)
    return v  # returns eigenvectors


print(compute_markov_chain(transition_matrix))
