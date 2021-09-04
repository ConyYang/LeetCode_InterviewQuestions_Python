class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        upper = self.upper(nums, target)
        lower = self.lower(nums, target)
        return [lower, upper]

    def lower(self, nums, t):
        left, right = 0, len(nums) - 1
        mid = 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= t:
                right = mid - 1
            else:
                left = mid + 1

        if left < 0 or left > len(nums) - 1:
            return -1
        elif nums[left] != t:
            return -1
        else:
            return left

    def upper(self, nums, t):
        left, right = 0, len(nums) - 1
        mid = 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0 or right > len(nums) - 1:
            return -1
        elif nums[right] != t:
            return -1
        else:
            return right

