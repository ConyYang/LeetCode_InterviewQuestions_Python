class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        if numRows == 1:
            return result

        base = [1, 1]
        result.append(base)

        for i in range(numRows - 2):
            newBase = [1]
            for b in range(len(base) - 1):
                newBase.append(base[b] + base[b + 1])
            newBase.append(1)
            result.append(newBase)
            base = newBase
        return result


a = Solution()
result = a.generate(5)
print(result)