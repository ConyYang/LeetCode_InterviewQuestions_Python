
def mergesort(A):
    len_A = len(A)
    if len_A <= 1:
        return A

    left = A[:len_A // 2]
    right = A[len_A // 2:]

    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        l = left[0]
        r = right[0]
        if l < r :
            result.append(l)
            left.remove(l)
        else:
            result.append(r)
            right.remove(r)

    result += left
    result += right
    print("result is {}".format(result))
    return result


A = [1, 4, 6, 3, 2, 7]
A = mergesort(A)
print(A)