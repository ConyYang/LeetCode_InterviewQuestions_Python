class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        count = 0
        while i<= n:
            count += n//i
            i *= 5
        return count