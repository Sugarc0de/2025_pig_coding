# Given a ground truth string, such as "I like dog", and another string "pig will like dog always",
# Compute the minimum edit distance (add, delete, update) for each word to make the input string equal
# to ground truth string. Print out the answer: how to make the changes and calculate word error rate.

# GT: I like a dog
# Input: Pig will like dog
# Edit distance: 3. Change "Pig" to "I"; Delete "will"; Add "a"

# DP[i, j] means the edit distance to make the sublist GT[:i+1] and Input[:j+1] equal
# Case1 : If GT[i] == INPUT[j], DP[i, j] = DP[i-1, j-1]
# Case2: If GT[i] != INPUT[j], Can either add a GT[i] or delete Input[j] or change INPUT[j]
# Base case: i == 0, j == 0 -> Edit distance: 0; i == 0, j > 0 -> Edit distance j + 1,
# i > 0, j == 0 -> Edit distance: i + 1


def solve(gt_s, src_s):
    dp = {}
    par = {}
    gt_lst = gt_s.split(" ")
    src_lst = src_s.split(" ")

    def reconstruct_sol():
        i, j = len(gt_lst) - 1, len(src_lst) - 1
        ans = []
        while i >= 0 or j >= 0:
            if i < 0:
                ans.append(f"DEL {src_lst[j]}")
                j -= 1
                continue
            if j < 0:
                ans.append(f"ADD {gt_lst[i]}")
                i -= 1
                continue
            op = par[(i, j)]
            if op == "no-ops":
                i -= 1
                j -= 1
            elif op == "add":
                ans.append(f"ADD {gt_lst[i]}")
                i -= 1
            elif op == "del":
                ans.append(f"DEL {src_lst[j]}")
                j -= 1
            else:
                ans.append(f"CHANGE {src_lst[j]} -> {gt_lst[i]}")
                i -= 1
                j -= 1

        return list(reversed(ans))

    def edit(i, j):
        if i < 0 and j < 0:
            return 0
        if i < 0 and j >= 0:
            return j + 1
        if j < 0 and i >= 0:
            return i + 1
        if (i, j) in dp:
            return dp[(i, j)]
        ans = 1e9
        if gt_lst[i] == src_lst[j]:
            par[(i, j)] = "no-ops"
            ans = edit(i - 1, j - 1)
        else:
            # min(add, delete, change)
            op = "no-ops"
            add_dist = edit(i - 1, j) + 1
            delete_dist = edit(i, j - 1) + 1
            change_dist = edit(i - 1, j - 1) + 1
            ans = min(add_dist, delete_dist, change_dist)
            if add_dist == ans:
                op = "add"
            elif delete_dist == ans:
                op = "del"
            else:
                op = "update"
            par[(i, j)] = (
                op  # gt list [:i+1] and source list [:j+1] are equal when the op was performed on index j
            )
        dp[(i, j)] = ans
        return ans

    ans = edit(len(gt_lst) - 1, len(src_lst) - 1)
    print(dp)
    # print(f"par: {par}")
    print(f"Target: {gt_s}; Input: {src_s}")
    print(reconstruct_sol())
    return ans


# print(solve("I like a dog", "Pig will always like dog"))  # 4
# print(solve("", "Pig will like dog"))  # 4
# print(solve("This is True", "Pig will like dog"))  # 4
print(solve("pig loves dog", "dog loves pig"))  # 2
# print(solve("a a b a a a", "a a a b a a"))
