def tenary_search(sorted_sequence, target):
    left = 0
    right = len(sorted_sequence) - 1
    while (left <= right):
        Third1 = (right-left)//3 + left
        Third2 = (right)