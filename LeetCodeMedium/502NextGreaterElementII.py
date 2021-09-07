class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(len(nums))]
        s = []
        for i in range(2 * n - 1, 0, -1):
            while (len(s) != 0 and s[-1] <= nums[i % n]):
                s.pop()
            if len(s) == 0:
                res[i % n] = -1
            else:
                res[i % n] = s[-1]
            s.append(nums[i % n])

        return res