class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        j = len(nums)-k
        nums_duplicate_part1 = nums[-k:]
        nums_duplicate_part2 = nums[:j]
        print(nums_duplicate_part1)
        print(nums_duplicate_part2)
        nums[-k:] =  nums_duplicate_part2
        nums[:j] = nums_duplicate_part1

