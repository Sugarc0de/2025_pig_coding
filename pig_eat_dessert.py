# The brute force n^2 solution
def pig_eat_dessert(desserts, M):
    count = 0
    for i in range(len(desserts) - 1):
        for j in range(i + 1, len(desserts)):
            if desserts[i] + desserts[j] >= M:
                print(
                    f"First dessert is {desserts[i]} and second dessert is {desserts[j]}"
                )
                count += 1
    return count


# Two pointers: sort the list in ascending order, left pointer starting from the index 0 and right pointer
# starts with the last position of the array. And everytime we find that desserts[left] + desserts[right] >- M;
# We count all the pairs from left to right - 1 to the right pointer. Then then we move the right pointer one
# position to the left, and keep counting; And if we find that desserts[left] + desserts[right] < M; we move the left
# pointer one position to the right; and we stop once left == right pointer.
def pig_eat_dessert_fast(desserts, M):
    desserts.sort()
    print(desserts)
    count = 0
    left_ix = 0
    right_ix = len(desserts) - 1
    while left_ix < right_ix:
        if desserts[left_ix] + desserts[right_ix] >= M:
            count += right_ix - left_ix
            right_ix -= 1
        else:
            left_ix += 1
    return count


# Implement binary search tomorrow
# You also need to sort them first.


def pig_eat_dessert_bs(desserts, M):
    count = 0
    desserts.sort()
    for ix, val in enumerate(desserts):
        low = ix
        high = len(desserts)
        target = M - val
        while high - low > 1:
            mid = (high + low) // 2
            if desserts[mid] >= target:
                high = mid
            else:
                low = mid
        count += len(desserts) - low - 1
    return count


def pig_eats(xs, T):
    xs = list(sorted(xs))
    ans = 0
    for i in range(len(xs)):
        xi = xs[i]
        # We want, at the end of binary search:
        # xs[lo] < T - xi
        # xs[hi] >= T - xi
        lo = i
        hi = len(xs)
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if xs[mid] < T - xi:
                lo = mid
            else:
                hi = mid
        ans += len(xs) - hi
    return ans


print(pig_eats([2, 4, 5, 1, 1, 4, 4, 7], 6))  # 19
print(pig_eats([2, 2, 2, 2], 4))  # 6
