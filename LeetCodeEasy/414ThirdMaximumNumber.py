class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(dict.fromkeys(nums))
        nums.sort()
        print(nums)
        try:
            result = nums[-3]
        except:
            result = nums[-1]
        return result