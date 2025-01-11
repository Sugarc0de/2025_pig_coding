# For each day, calculate the max cash or max pigcoin, and at the last day, get the max cash.
# Iterative DP


def buy_pigcoin(rates, cash, fee):
    dp = {}
    for ix, r in enumerate(rates):
        if ix == 0:
            max_cash = cash
            max_pigcoin = (cash - fee) / rates[ix]
            dp[ix] = (max_cash, max_pigcoin)
        else:
            pre_max_cash, pre_max_pigcoin = dp[ix - 1]
            max_cash = max(pre_max_cash, pre_max_pigcoin * rates[ix] - fee)
            max_pigcoin = max(pre_max_pigcoin, (pre_max_cash - fee) / rates[ix])
            dp[ix] = (max_cash, max_pigcoin)
    return dp[len(rates) - 1][0]


# Solution two: DP with recursion?


# only one day, 2
print(buy_pigcoin([5], 2, 3))

# 2, can't buy anything
print(buy_pigcoin([1, 5], 2, 3))

# 47 after buying and selling
print(buy_pigcoin([1, 5], 13, 3))

# 47, same answer
print(buy_pigcoin([3, 2, 1, 5, 4], 13, 3))

# 80, double it 3 times
print(buy_pigcoin([2, 1, 2, 1, 2, 1, 2], 10, 0))
