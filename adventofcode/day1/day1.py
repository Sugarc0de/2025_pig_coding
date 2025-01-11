from collections import defaultdict


def read_input_from_txt(filename):
    lst1 = []
    lst2 = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.rstrip().split(" ")
            i = int(line[0])
            j = int(line[-1])
            lst1.append(i)
            lst2.append(j)
    return lst1, lst2


def part_one():
    lst1, lst2 = read_input_from_txt("./input.txt")

    lst1 = list(sorted(lst1))
    lst2 = list(sorted(lst2))

    diff = 0
    for ix in range(len(lst1)):
        max_num = max(lst1[ix], lst2[ix])
        min_num = min(lst1[ix], lst2[ix])
        diff += max_num - min_num
    return diff


def part_two():
    lst1, lst2 = read_input_from_txt("./input.txt")
    d2 = defaultdict(int)
    for val in lst2:
        d2[val] += 1
    sim_score = 0
    for val in lst1:
        sim_score += val * d2[val]
    return sim_score


print(part_two())
