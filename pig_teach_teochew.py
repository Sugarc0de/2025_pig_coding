# Write a encoder to teach teochew count from 0 to 5 million. So dog will give a number, and
# the program should output the correct teochew characters -- as pig is teaching it.

BASIC_NUMBER = {
    1: "yi",
    2: "noa",
    3: "san",
    4: "si",
    5: "ngo",
    6: "lek",
    7: "qi",
    8: "boi",
    9: "gou",
    10: "zao",
    11: "zao yi",
    12: "zao er",
    20: "er zao",
    30: "san zao",
    40: "si zao",
    50: "ngo zao",
    60: "lek zao",
    70: "qi zao",
    80: "boi zao",
    90: "gou zao",
    100: "zek bei",
    200: "noa bei",
    300: "san bei",
    400: "si bei",
    500: "ngo bei",
}

BIG_NUMBER = {
    100: "bei",
    1000: "chia",
    10000: "muang",
}


# Given the num, produce the sound
def solve(num):
    itos = []

    def recur(num):
        if num == 0:
            return
        if num == 2 and len(itos) > 0:
            # special case such as 22, 32, ..., 92
            itos.append("er")
            return
        if num in BASIC_NUMBER:
            itos.append(BASIC_NUMBER[num])
            return
        q, r = 0, 0
        big_num = None
        if num > 10 and num <= 100:
            q = num // 10
            r = num % 10
            big_num = 10
            if q == 1 and len(itos) > 1:
                # special case such as 114: zek bei "yi" zao si
                itos.append("yi")
        elif num > 100 and num <= 1000:
            q = num // 100
            r = num % 100
            big_num = 100
        elif num > 1000 and num <= 10000:
            q = num // 1000
            r = num % 1000
            big_num = 1000
        elif num > 10000:
            q = num // 10000
            r = num % 10000
            big_num = 10000

        recur(r)
        return

    recur(num)
    return " ".join(itos)


# for num in range(1000000, 1030000):
#     print(f"{num} : ", solve(num))

import random

for i in range(10):
    x = random.randint(1, 5000000)
    print(x, solve(x))
