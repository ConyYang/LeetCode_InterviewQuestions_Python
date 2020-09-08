class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_len = len(nums)
        if num_len <= 1:
            return nums
        left = nums[:num_len // 2]
        right = nums[num_len // 2:]

        left = self.sortArray(left)
        right = self.sortArray(right)
        return self.merge(left, right)

    def merge(self, left, right):
        arr = []
        while left and right:
            l = left[0]
            r = right[0]
            if l < r:
                arr.append(l)
                left.pop(0)
            else:
                arr.append(r)
                right.pop(0)
        arr += left
        arr += right
        return arr