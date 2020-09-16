class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s == t