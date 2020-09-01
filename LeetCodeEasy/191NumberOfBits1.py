class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for _ in range(32):
            if n & 1:
                count +=1
            n >>=1
        return count