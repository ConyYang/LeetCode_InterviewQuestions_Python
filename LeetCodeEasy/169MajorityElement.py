class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        dict_num = {}
        times = len(nums) / 2
        for n in nums:
            if n not in dict_num:
                dict_num[n] = 1
            else:
                dict_num[n] += 1
                if dict_num[n] > times:
                    return n