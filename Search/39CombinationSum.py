class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self,candidates, target, start_index, cur, result):
        if target == 0:
            result.append(cur)
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > target:
                continue
            self.dfs(candidates, target - candidates[i], i, cur + [candidates[i]], result)


a = Solution()
result = a.combinationSum([2,3,6,7], 7)
print(result)