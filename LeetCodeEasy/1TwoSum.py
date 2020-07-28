class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #         index_1 = 0
        #         for num_1 in nums:
        #             index_2 = index_1 + 1
        #             for num_2 in nums[index_2:]:
        #                 if num_2 + num_1 == target:
        #                     return [index_1, index_2]
        #                 index_2 += 1
        #             index_1 += 1

        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]