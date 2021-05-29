def checkPalindromeFormation(a, b):
    """
    :type a: str
    :type b: str
    :rtype: bool
    """
    if len(a) == 1 or len(b) == 1:
        return True
    for i in range(len(a)):
        a_prefix = a[:i]
        a_suffix = a[i:]
        b_prefix = b[:i]
        b_suffix = b[i:]

        if a_prefix[::-1] == b_suffix or a_suffix[::-1] == b_prefix:
            return True


if __name__ == '__main__':
    ans = checkPalindromeFormation("ulacfd","jizalu")
    print(ans)