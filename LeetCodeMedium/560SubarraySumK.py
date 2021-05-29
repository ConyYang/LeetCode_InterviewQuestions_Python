def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    map_count = {0:1}

    ans = 0
    sum_curr = 0

    for n in nums:
        sum_curr += n
        check = sum_curr - k
        if check in map_count:
            ans += map_count[check]
        if sum_curr not in map_count:
            map_count[sum_curr] = 1
        else:
            map_count[sum_curr] += 1
    return ans



a  = subarraySum([1,1,-1,1],1)
print(a)