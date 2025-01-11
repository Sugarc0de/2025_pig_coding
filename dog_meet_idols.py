# idols1 = [1, 2, 3, 4]
# ans1 = 4

# idols2 = [0, 12]
# ans2 = 2

# idols3 = [1, 5, 10, 13, 18]

# idol_counter = list(range(0, 25)) #

# # cover the period to meet idol
# left_idx = 0
# right_idx =  11

# left_idx = 1
# right_idx = 12

# left_idx = 13
# right_idx = 13 + 11 = 25 - 25 = 0 (left_idx)


# [3, 0, 0, 12, 15, 18, 21, 24] # 0 - 24


def dog_meets_idol(idols_time):
    max_hours = 24
    idols_per_hour = [0] * max_hours
    for idol_time in idols_time:
        idols_per_hour[idol_time] += 1
    idols_per_hour_double = idols_per_hour + idols_per_hour
    # Sliding window approach
    max_idols, curr_max_idols = 0, 0
    start_idx, end_idx = 0, 11
    while start_idx < max_hours:
        curr_max_idols = sum(idols_per_hour_double[start_idx : end_idx + 1])
        if curr_max_idols > max_idols:
            print(
                "The best start idx is ",
                start_idx,
                " and the best end idx is ",
                end_idx,
            )
            max_idols = curr_max_idols
        start_idx += 1
        end_idx += 1
    return max_idols


idols_time = [1, 1, 5, 5, 11, 16, 23, 23]
print(dog_meets_idol(idols_time))
