class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                compare_index = mid + 1
            else:
                compare_index = mid - 1
            if nums[compare_index] == nums[mid]:
                start = mid + 1
            else:
                end = mid
        return nums[start]


a = Solution()
result = a.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11])
print(result)
