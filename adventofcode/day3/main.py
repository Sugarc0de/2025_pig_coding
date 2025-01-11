def read_input_from_txt(filename):
    with open(filename, "r") as f:
        data = f.read().replace("\n", "")
    return data


def solve():
    data = read_input_from_txt("input.txt")
    stack = []
    results = 0
    lnum, rnum = None, None
    for c in data:
        if c == "(":
            if len(stack) >= 3 and stack[-3:] == ["m", "u", "l"]:
                stack = []
                stack.append("(")
            else:
                stack = []  # clear the stack
        elif c == ",":
            if (
                len(stack)
                and stack[0] == "("
                and " " not in stack
                and "".join(stack[1:]).isnumeric()
            ):
                lnum = eval("".join(stack[1:]))
                stack = [stack[0]]  # clear the stack
        elif c == ")":
            if (
                len(stack)
                and stack[0] == "("
                and " " not in stack
                and "".join(stack[1:]).isnumeric()
            ):
                rnum = eval("".join(stack[1:]))
            if lnum and rnum:
                results += lnum * rnum
                lnum, rnum = None, None
            stack = []  # Clear the stack regardless
            continue
        elif c == "0" and len(stack) and stack[-1] == "(":
            stack = []
        else:
            stack.append(c)
    return results


print(solve())
