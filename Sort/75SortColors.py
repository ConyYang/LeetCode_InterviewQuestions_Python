from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_index = 0
        while current_index < len(nums) - 1:
            minimum_index = current_index
            for i in range(current_index + 1, len(nums)):
                if nums[minimum_index] > nums[i]:
                    minimum_index = i
            nums[current_index], nums[minimum_index] = nums[minimum_index], nums[current_index]
            current_index += 1