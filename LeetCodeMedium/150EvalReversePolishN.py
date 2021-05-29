def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for t in tokens:
        if (t!="+" and t!= "-" and t!="*" and t!="/"):
            stack.append(int(t))
        else:
            a2 = stack.pop()
            a1 = stack.pop()
            if (t == "+"):
                stack.append(a1 + a2)
            elif (t == "-"):
                stack.append(a1 - a2)
            elif (t == "*"):
                stack.append(a1 * a2)
            else:
                stack.append(int(a1 / a2))
    return stack[-1]


ans = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(ans)