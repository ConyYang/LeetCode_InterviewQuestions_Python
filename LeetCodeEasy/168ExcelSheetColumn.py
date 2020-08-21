class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ""
        while (n > 26):
            residue = n % 26
            result += chr(65 + residue)
            n = n // 26
        n = n // 26
        result += chr(64 + n)
        return result[::-1]


a = Solution()
result = a.convertToTitle(701)
print(result)