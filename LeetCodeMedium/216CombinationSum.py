class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(k, n, s, cur, ans):
            if k == 0 and n == 0:
                ans.append(list(cur))
            for i in range(s, min(n + 1, 10)):
                dfs(k - 1, n - i, i + 1, cur + [i], ans)

        ans = []
        dfs(k, n, 1, [], ans)
        return ans

if __name__ == '__main__':
    a = Solution()
    ans = a.combinationSum3(3, 9)
    print(ans)
