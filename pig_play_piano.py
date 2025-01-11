# (note, start, duration)
notes1 = [(7, 1, 3), (8, 2, 0), (20, 10, 2), (24, 12, 1)]
ans1 = True

notes2 = [
    (8, 10, 1),
    (8, 9, 2),
    (15, 14, 1),
    (30, 12, 3),
]  # (12, 1, 30), (14, 1, 15), (15, -1, 15), (15, -1, 30)
ans2 = False

notes3 = [(8, 10, 1), (20, 11, 2)]
ans3 = True


def pig_play_piano(notes):
    data = []
    for note, start, duration in notes:
        data.append((start, 1, note))  # Add the note at start time
        data.append((start + duration, -1, note))  # Remove the note at end time
    # print("Original data is ", data)
    # Sorting by the first item in ascending order, second item in descending order.Cuz you want to add the notes before removing
    diff = sorted(data, key=lambda x: (x[0], -x[1]))
    # print("diff is ", diff)
    counter = []

    curr_ts = diff[0][0]
    for ts, change, note in diff:
        if curr_ts != ts:
            curr_ts = ts
            if len(counter) and max(counter) - min(counter) > 10:
                return False
        if change == 1:
            counter.append(note)
        elif change == -1:
            counter.remove(
                note
            )  # Remove the first occurence if there are more than one match
    return True


# Github version (This version assume that you can move super fast from one note to another so release to play another note)
def can_play(notes):
    diff = []
    for note, start, duration in notes:
        diff.append((start, 1, note))
        diff.append((start + duration, -1, note))
    diff = list(sorted(diff))
    print("diff is ", diff)
    values = (
        set()
    )  # A set is okay here because you do not play on the same note at the same time
    for ts, change, note in diff:
        if change == 1:
            values.add(note)
        elif change == -1:
            values.remove(note)
        if (
            len(values) > 0 and max(values) - min(values) > 10
        ):  # pig only has 10 fingers
            return False
    return True


print(pig_play_piano(notes1))
print(pig_play_piano(notes2))
print(pig_play_piano(notes3))
