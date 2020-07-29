class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)

        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i

a = Solution()
i = a.searchInsert([1,3,5,6], 5)
print(i)