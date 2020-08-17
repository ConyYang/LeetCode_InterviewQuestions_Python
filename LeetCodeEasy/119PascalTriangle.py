class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        result = [1]
        if rowIndex == 0:
            return result

        base = [1, 1]
        result = base
        for i in range(rowIndex - 1):
            result = [1]
            for b in range(len(base) - 1):
                result.append(base[b] + base[b + 1])
            result.append(1)
            base = result
        return result


a = Solution()
result = a.getRow(5)
print(result)