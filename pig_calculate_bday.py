# Given a frend's birthday, month and day.
# Print out the string representing the day of the week
# for this year and next year.

# SPEED CHALLENGE

days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def wday(month, day):
    # 2, 14
    start_wday_2025 = ["wed", "thurs", "fri", "sat", "sun", "mon", "tues"]
    start_wday_2026 = ["thurs", "fri", "sat", "sun", "mon", "tues", "wed"]

    days = day + sum(days_per_month[0:month])  # Feb, add up all the Jan

    while days > 7:
        days = days - 7

    wday_2025 = start_wday_2025[days - 1]
    wday_2026 = start_wday_2026[days - 1]

    return wday_2025, wday_2026


print(wday(1, 30))
print(wday(2, 14))
print(wday(8, 31))
print(wday(10, 17))
