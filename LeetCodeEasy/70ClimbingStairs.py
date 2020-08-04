class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev_1 = 1
        prev_2 = 2
        if n == 1:
            return prev_1
        elif n == 2:
            return prev_2
        for i in range(n-2):
            cur = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = cur
        return cur


a = Solution()
result = a.climbStairs(38)
print(result)