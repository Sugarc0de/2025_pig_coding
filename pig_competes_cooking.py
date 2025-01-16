# Pig enters into a cooking contest and she tries to win. Each contestant has a skill level (real number between 0 and 10).
# Multiple people can have the same skill levels. At most one people can advance to the next level. Here is the rule: the
# judge will randomly the order to evaluate people's cooking. And he will always eliminate the first person. And as soon as
# he sees another person with skill more than 1 level better than the first person, he will select this person and automatically
# eliminate the rest people. Compute the probability that each person will advance to the next game.
# [difficulty=5] O(n^2) solution
# [difficulty=7] O(n) solution
# Example: [1, 4, 4, 6]
# Answer: [0, 1/12, 1/12, 7/12]


# O(n) the optimal solution
def solve(levels):
    # Once we select the first person, we can ignore the non-eligible ones, and assign equal probability to the eligible ones.
    # Use two pointers to first get a number of contestants that are eligible for each of the current level.
    eligible = [0 for _ in range(len(levels))]
    i, j = 0, 1
    while i < len(levels):
        if j >= len(levels):
            i += 1
            continue
        if levels[i] + 1 <= levels[j]:
            eligible[i] += len(levels) - j
            i += 1
        else:
            j += 1

    print(eligible)
    # Now that we have a list of eligible contestants for each person chosen as the first one, we can use prefix sum
    # t0 calculate the probability.
    prefix_sum = [0 for _ in range(len(eligible))]
    for curr_ix in range(len(eligible)):
        # Add from previous prefix sum
        if curr_ix > 0:
            prefix_sum[curr_ix] += prefix_sum[curr_ix - 1]
        if eligible[curr_ix] > 0:
            target_ix = len(eligible) - eligible[curr_ix]
            prefix_sum[target_ix] += 1 / eligible[curr_ix]
    return [1 / len(levels) * prob for prob in prefix_sum]


print(solve([1, 1.5, 2, 2, 2, 2.5, 3, 3, 3.5, 5, 6, 6.4, 6.5, 6.6, 8, 9]))
