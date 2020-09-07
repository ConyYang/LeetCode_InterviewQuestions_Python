class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max, cur_max = 0, 0
        for num in nums:
            last_max, cur_max = cur_max, max(last_max+num, cur_max)
        return cur_max