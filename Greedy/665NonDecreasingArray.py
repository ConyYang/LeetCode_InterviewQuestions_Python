class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        error = 0
        index = 1
        for val in nums[1:]:

            if nums[index - 1] > nums[index]:
                error += 1
                if error > 1:
                    return False
                if index < 2 or nums[index - 2] <= nums[index]:
                    nums[index - 1] = nums[index]
                else:
                    nums[index] = nums[index - 1]

            index += 1

        return True