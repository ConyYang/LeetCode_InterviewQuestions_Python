class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]

        if len(nums) == 1:
            return temp

        num_compare = []
        num_compare.append(temp)

        for a in nums[1:]:
            if a not in num_compare:
                num_compare.append(a)
            else:
                num_compare.remove(a)
        return num_compare[0]


a = Solution()
result = a.singleNumber([4, 1, 2, 1, 2])
print(result)
