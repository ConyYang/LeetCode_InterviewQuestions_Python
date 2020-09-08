
A = [64, 34, 25, 12, 22, 11, 90]

B = [64, 34, 25, 12, 22, 11, 90]


def BubbleSort(A):
    for i in range(len(A), 0, -1):
        for j in range(1, i):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]


def BubbleSort2(B):
    for i in range(len(B)):
        for j in range(len(B) - i - 1):
            if B[j + 1] < B[j]:
                B[j + 1], B[j] = B[j], B[j + 1]


BubbleSort(A)
print(A)

BubbleSort(B)
print(B)