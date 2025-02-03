# Dog wants to divide his money into exactly half and give pig half of his money.
# Money is written inside a string, which can be "0.045" or "12340", returns the
# half amount in string. Cannot use multiplication or convert the entire string to int to solve.
# Difficulty: 2.5


def solve(money):
    ans = []
    carry_over = 0
    has_decimal = False
    for char in money:
        if char == ".":
            has_decimal = True
            if len(ans) == 0:
                ans.append("0")
            ans.append(char)
        else:
            num = int(char)
            if carry_over > 0:
                num = carry_over * 10 + num
            curr_digit = num // 2
            carry_over = num % 2
            if curr_digit == 0 and len(ans) == 0:
                continue
            ans.append(str(curr_digit))
    if carry_over > 0:
        if not has_decimal:
            has_decimal = True
            ans.append(".")
        num = carry_over * 10
        curr_digit = num // 2
        ans.append(str(curr_digit))
        assert num % 2 == 0
    return "".join(ans)


print(solve("26"))
print(solve("0.01"))
print(solve("51"))
print(solve("12359.32"))
print(solve("0.043"))

for x in range(100):
    t = x * 2.7 + 0.3 / 7
    print(t, solve(str(t)))
