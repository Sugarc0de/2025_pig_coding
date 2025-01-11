def read_input(filename):
    L = []
    with open(filename, "r") as f:
        for l in f.readlines():
            L.append([int(i) for i in l.rstrip().split(" ")])

    return L


def main():
    L = read_input("input.txt")
    num_safe = 0
    for level in L:
        i = 0
        j = 1
        diff = level[j] - level[i]
        unsafe = False
        while j < len(level):
            # If true, it means it is neither decreasing nor increasing
            if (level[j] - level[i]) * diff <= 0:
                unsafe = True
                break  # this level is unsafe
            if abs(level[j] - level[i]) > 3:
                unsafe = True
                break  # unsafe level
            diff = level[j] - level[i]
            i += 1
            j += 1
        if not unsafe:
            num_safe += 1

    return num_safe


print(main())
