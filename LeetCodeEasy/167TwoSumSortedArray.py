class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        result_sum = numbers[start] + numbers[end]
        while (result_sum) != target:
            if result_sum > target:
                end -= 1
            else:
                start += 1
            result_sum = numbers[start] + numbers[end]
        return [start + 1, end + 1]


a = Solution()
result = a.twoSum([2, 7, 11, 15], 9)
print(result)
