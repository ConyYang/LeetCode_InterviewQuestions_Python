class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num:
                nums[index] = num
                index += 1
        nums[index:] = [0] * (len(nums) - index)


a = Solution()
list_test = [0, 1, 0, 3, 12]
a.moveZeroes(list_test)
print(list_test)
