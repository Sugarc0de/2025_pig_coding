# pig has a list of taylor swift's songs and she sees it everywhere.
# Give a list of her songs, and an text. Find as many words as possible.
# TAYLOR
# SWIFT
# STYLE
# LOVER
# CALMDOWN
# WILLOW
# ANTIHERO
# CARDIGAN
# BETTY
# ENCHANTED
# LOVESTORY

# input:
# model-assisted forest inventory models are enchanting with nonlinear data
# output:
# model-asSisTed forest inventorY modeLs arE ENCHANTing with nonlinEar Data
#         S  T                  Y     L    E ENCHANT               E   D


# The idea is that you keep track of multiple pointers, one for each word,
# Everytime you see a character that matches the corresponding pointer position
# of the word(s), you move the pointer one place forward. Stop when you find the
# first word that ends, and you reset all the pointers to that ending index position
# before restarting the process again. For each pointer, you need to know what word
# it is tracking, and the position, after you find the first word, can add all the
# positions to a list.

# can be a dictionary, {word: [0, 4, 10, -- positions of the characters of the partial words]}
# For example, {"swift": [0, 6, 10]}


input = "model-assisted forest inventory models are enchanting with nonlinear data"
words = [
    "taylor",
    "swift",
    "lover",
    "calmdown",
    "willow",
    "antihero",
    "style",
    "enchanted",
]

input2 = "Textbook on classical statistical methods for working with time series, mainly focusing on autoregressive, moving average, exponential smoothing, and regression-based models. This book is overall fairly easy to read while being mathematically rigorous and provides examples of working with time series in various statistical packages like JMP, SAS, and R. The examples are quite detailed (maybe overly so, with many pages in each chapter just displaying full datasets in a table of numbers, not sure what the point of this is). Although examples are given in R, the book does not use any modern packages related to time series and instead focuses on doing it manually, which is good for educational purposes but not the most practical as it goes into detail about steps for manually identifying ARIMA models rather than using more automated approaches; it also does not cover any machine learning methods for working with time series, only the classical statistical methods."


def solve(input, words):
    input = input.lower()
    found = []
    count = 0
    track = {key: [] for key in words}
    for i, char in enumerate(input):
        for key in track:
            # print("current key is ", key)
            # print("curr char is ", char)
            # print("curr track: ", track)
            clen = len(track[key])
            wlen = len(key)
            # If the current char of the input matches with the character that the word is needing next
            if clen < wlen and char == key[clen]:
                track[key].append(i)
                if clen + 1 == wlen:
                    # print("clen == wlen: ", found)
                    found.extend(track[key])
                    count += 1
                    track = {key: [] for key in words}
                    break
    formatted = list([char for char in input])
    # print("formatted: ", formatted)
    # print("found: ", found)
    for _, ix in enumerate(found):
        formatted[ix] = input[ix].upper()
    return count, "".join(formatted)


print(solve(input2, words))
