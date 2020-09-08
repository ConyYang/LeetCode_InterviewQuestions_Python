A = [1, 8, 3, 9, 4, 5, 7]


def QuickSort(A, low, high):
    if len(A) == 1:
        return
    if low < high:
        pivot_idx = partition(A, low, high)
        QuickSort(A, low, pivot_idx-1)
        QuickSort(A, pivot_idx+1, high)


def partition(arr, low, high):
    i = low - 1
    pivot_val = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot_val:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[high], arr[i] = arr[i], arr[high]
    return i


QuickSort(A, 0, len(A)-1)
print(A)