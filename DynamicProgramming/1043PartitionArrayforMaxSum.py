def maxSumAfterPartitioning(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    dp = [0 for _ in range(len(arr) + 1)]

    for i in range(1, len(arr) + 1):
        curr_max = 0
        for j in range(1, min(i, k)+1):
            curr_max = max(curr_max, arr[i-j])
            dp[i] = max(dp[i], dp[i-j] + curr_max *j)

    return dp[-1]


result = maxSumAfterPartitioning([2, 1, 4, 3], 3)
print(result)
