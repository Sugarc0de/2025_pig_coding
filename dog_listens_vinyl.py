# What position to put the needle. THe vinyl has radius 6 inches,
# needle position 0 - 6, 0 being the outest, and it can have float number as position.
# Albums has a list of songs with the length, length is the number of minutes (e.g. 1.85)
# Each minute of a song corresponds to one square inch of areas on the vinyl. Determine
# the needle position of the songs, or return [] if all the songs cannot be fit.
import math

PI = math.pi

VINYL_RADIUS = 6
VINYL_AREA = PI * VINYL_RADIUS**2

songs = [
    ("blue", 11 * PI),
    ("lunch", 16 * PI),
    ("guess", 9 * PI),
    # ("chinoro", 5),
    # ("greatest", 5),
]


def solve(songs):
    total_song_area = 0
    for name, length in songs:
        total_song_area += length  # 1 minute = 1 square inch
    if total_song_area > VINYL_AREA:
        return []
    song_widths = []
    remaining_area = VINYL_AREA
    remaining_radius = VINYL_RADIUS
    print("vinyl area: ", remaining_area)
    for name, length in songs:
        curr_song_area = length  # 1 min = 1 square inch
        remaining_area = remaining_area - curr_song_area
        print("name: ", name)
        print("length: ", length)
        print("remaining area: ", remaining_area)
        song_width = remaining_radius - math.sqrt(remaining_area / PI)
        song_widths.append([name, song_width])
        remaining_radius = math.sqrt(remaining_area / PI)
    needle_position = []
    acc_width = 0
    for name, width in song_widths:
        curr_position = width + acc_width
        needle_position.append([name, curr_position])
        acc_width = curr_position
    return needle_position


print(solve(songs))
