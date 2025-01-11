t = [("meat", 4, 7), ("pepper", 5, 3), ("cabbage", 5, 2), ("green onions", 1, 1)]


def optimize_cooking(food_time):
    # Sort by preparation time in descending order
    sorted_time = sorted(food_time, key=lambda x: x[2], reverse=True)
    print(sorted_time)
    optimum_cook_time = 0
    prev_cook_time = 0
    idx = 0
    while idx < len(sorted_time):
        curr_cook_time = prev_cook_time + sorted_time[idx][1] + sorted_time[idx][2]
        if curr_cook_time > optimum_cook_time:
            optimum_cook_time = curr_cook_time
        prev_cook_time = prev_cook_time + sorted_time[idx][1]
        idx += 1
    return optimum_cook_time


print(optimize_cooking(t))
