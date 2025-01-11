hotels = [-1, -3, 0, 4, 5]
dist = 2


# Two pointers but only linear time
def pig_book_hotel(hotels, dist):
    ans = 0
    hotels.sort()
    print("sorted hotels: ", hotels)
    j = 1
    # i is pig's location
    for i in range(len(hotels)):
        # j is dog's location, everytime j starts from where it
        # last stands, not i + 1
        while j < len(hotels) and hotels[j] - hotels[i] <= dist:
            j += 1
        # j falls off too far from i
        ans += j - i - 1
    return ans


def pig_book_hotel_bs(hotels, dist):
    # We always want to keep:
    # lo <= dist - xi and
    # hi > dist - xi
    lst = list(sorted(hotels))
    ans = 0
    for i in range(len(lst)):
        xi = lst[i]
        lo = i
        hi = len(lst)
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if lst[mid] - xi <= dist:  # be careful about negative and positive numbers
                lo = mid
            else:
                hi = mid
        ans += lo - i
    return ans


# negative values, 3
print(pig_book_hotel_bs([-1, -3, 0, 4, 5], 2))

# no value, 0
print(pig_book_hotel_bs([1, 4, 6, 9, 11], 1))

# dup values, 17
print(pig_book_hotel_bs([-2, -2, 0, 1, 3, 3, 6.5], 5))
