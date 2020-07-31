def maxSubarray(nums):
    if max(nums) < 0:
        return max(nums)
    else:
        # cur_max = max(nums)
        # for i in range(len(nums)):
        #     for k in range(len(nums)+1):
        #         if nums[i:k] and sum(nums[i:k]) > cur_max:
        #             cur_max = sum(nums[i:k])
        # return cur_max

        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(local_max + num, 0)
            global_max = max(local_max, global_max)
        return global_max


sum = maxSubarray([1, 2, 3, 4])
print(sum)
