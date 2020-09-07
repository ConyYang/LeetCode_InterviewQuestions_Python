A = [7, 8, 5, 4, 9, 2]
# Start with the
# loop: 8 are in right position
# swap 5 with 8 and 7 to make it to right position


def insertion_sort(A):
    for i in range(1, len(A)):
        # print(i)
        for j in range(i-1, 0, -1):
            print(j)
            if A[i] > A[j+1]:
                # print(A[i])
                A[i], A[j+1] = A[j+1], A[i]
            else:
                break
    return A

insertion_sort(A)