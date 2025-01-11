# Input: [timestamp (int), concert_name (string)]
# each concert will get rate limited so max 3 allowed per min
# all concert will get rate limited so max 5 concert check allowed per min
# Decide which input will be rate limited, return a list of true (= "pass") and false (= "rate limited")

# eg: [[0, "red"], [5, "blue"], [2, "red"]]

events = [[0, "red"], [10, "red"], [15, "yellow"], [20, "red"], [30, "red"]]

max_allowed_for_all_concerts = 5
max_allowed_for_each_concert = 3


# The idea of rate limiting goes like this:
# Two pointer i and j. Keep the sliding window of 60s
# Maintain a dictionary over the window.
def rate_limit(events):
    ans = []
    i = 0
    j = i
    counter = {}
    while i < len(events):
        start_ts = events[i][0]
        end_ts = start_ts + 60
        while j < len(events) and events[j][0] < end_ts:
            name = events[j][1]
            if (
                sum([len(i) for i in list(counter.values())])
                == max_allowed_for_all_concerts
            ):
                ans.append([events[j][0], name, False])
            elif name not in counter:
                counter[name] = set([events[j][0]])
                ans.append([events[j][0], name, True])
            elif name in counter:
                if len(counter[name]) == max_allowed_for_each_concert:
                    ans.append([events[j][0], name, False])
                else:
                    counter[name].add(events[j][0])
                    ans.append([events[j][0], name, True])
            j += 1
        if events[i][0] in counter[events[i][1]]:
            counter[events[i][1]].remove(events[i][0])
        i += 1
    return ans


events = [
    (0, "a"),
    (1, "a"),
    (59, "a"),
    (60, "a"),
    (61, "a"),
    (62, "a"),
    (63, "a"),
    (64, "a"),
]

for ts, name, ans in rate_limit(events):
    print(ts, name, ans)
