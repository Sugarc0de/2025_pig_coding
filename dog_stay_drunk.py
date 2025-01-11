# Dog gives a list of drinks with different alcohol. Ane the alcohol inside his body decays exponentially with half life equal to 30 mins.
# First drink at time 0, and when the alcohol in his body goes below 10 (or equal to 10), he takes another drink. What is the time stamp that he takes
# each drink.

# y = A0*e^(-kt)
# half life = ln2 / k
import math


def solve(drinks, half_time):
    k = math.log(2) / half_time
    time_interval = []
    time_interval.append(0)
    threshold = 10
    A0 = 0
    for drink in drinks:
        # y = A0*e^(-kt)
        A0 += drink
        if A0 <= threshold:
            last_t = time_interval[-1] if time_interval else 0
            time_interval.append(last_t)
            continue
        t = math.log(threshold / A0) / (-k)
        A0 = threshold
        time_interval.append(t)

    ans = []
    total_time_so_far = 0
    for time in time_interval:
        total_time_so_far += time
        ans.append(total_time_so_far)
    return ans


print(solve([3, 12, 7, 10, 20], 30))

print(solve([20, 40, 60], 10))

print(solve([2, 4, 3, 91], 2))

print(solve([10, 10, 10, 10], 10))
