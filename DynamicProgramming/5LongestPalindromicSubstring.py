class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            odd = self.getlongest(s, i, i)
            even = self.getlongest(s, i, i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result
    def getlongest(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]