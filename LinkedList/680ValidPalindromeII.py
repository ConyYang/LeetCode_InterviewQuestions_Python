class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return s[l:r]==s[l:r][::-1] or s[l+1:r+1]==s[l+1:r+1][::-1]
        return True