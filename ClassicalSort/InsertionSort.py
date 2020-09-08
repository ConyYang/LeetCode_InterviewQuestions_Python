A = [7, 3, 4, 1, 2]


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


insertion_sort(A)
print(A)
