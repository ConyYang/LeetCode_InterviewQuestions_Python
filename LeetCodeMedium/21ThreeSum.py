class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        lengh = len(nums)
        dict_count = {}

        for n in nums:
            if n in dict_count:
                dict_count[n] += 1
            else:
                dict_count[n] = 1

        ans = []

        for i in range(lengh):
            if i and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, lengh):
                if j - i != 1 and nums[j] == nums[j - 1]: continue

                target = 0 - nums[i] - nums[j]

                if target < nums[j]: continue
                if target not in dict_count: continue

                if (dict_count[target] - (nums[i] == target) - (nums[j] == target)) >= 1:
                    ans.append([nums[i], nums[j], target])

        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]


    s = Solution()
    ans = s.threeSum(nums)
    print(ans)
