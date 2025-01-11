# There are 60 mins total and three time setting for the chess game: blitz, rapid, classic.
# Blitz is 5 mins, rapid 10 mins and classic 15 mins and dog has winning probability of
# 40%, 50%, 60% for each game setting. And if he loses 3 games in total, he is out. Q: under
# optimum playing strategy, what is the expected number of wins under 60 mins.

BLITZ_TIME = 5
RAPID_TIME = 10
CLASSIC_TIME = 15


def solve(
    total_time_limit, blitz_win_prob, rapid_win_prob, classic_win_prob, max_num_loses
):
    dp = {}

    # return the highest expected win given the time limit and how many more losses are allowed
    def recur(time_limit, remaining_loses):
        if (time_limit, remaining_loses) in dp:
            return dp[(time_limit, remaining_loses)]

        if remaining_loses <= 0 or time_limit <= 0:
            dp[(time_limit, remaining_loses)] = 0  # Cannot play anymore
            return 0

        else:
            expected_win_blitz = blitz_win_prob * (
                1 + recur(time_limit - BLITZ_TIME, remaining_loses)
            ) + (1 - blitz_win_prob) * recur(
                time_limit - BLITZ_TIME, remaining_loses - 1
            )

            expected_win_rapid = rapid_win_prob * (
                1 + recur(time_limit - RAPID_TIME, remaining_loses)
            ) + (1 - rapid_win_prob) * recur(
                time_limit - RAPID_TIME, remaining_loses - 1
            )

            expected_win_classic = classic_win_prob * (
                1 + recur(time_limit - CLASSIC_TIME, remaining_loses)
            ) + (1 - classic_win_prob) * recur(
                time_limit - CLASSIC_TIME, remaining_loses - 1
            )

            dp[(time_limit, remaining_loses)] = max(
                expected_win_blitz, expected_win_rapid, expected_win_classic
            )

        return dp[(time_limit, remaining_loses)]

    recur(total_time_limit, max_num_loses)
    return dp[(total_time_limit, max_num_loses)]


print(solve(60, 0.4, 0.5, 0.6, 3))
print(solve(60, 0.4, 0.5, 0.6, 1))
print(solve(10, 0.4, 0.5, 0.6, 1))
