class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        last = len(nums) - 1
        while start <= last:
            print('Start{}'.format(start))
            print('Last{}'.format(last))
            if nums[start] == val:
                # swap
                nums[start], nums[last] = nums[last], nums[start]
                last -= 1
            else:
                start += 1
        return start

a = Solution()
nums = [3,2,2,3]
start = a.removeElement(nums=nums, val=3)
print('result')
print(nums[:start])