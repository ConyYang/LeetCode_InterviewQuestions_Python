class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s1 = ""
        s2 = ""
        for i_s in s:
            if (i_s >= 'a' and i_s <= 'z') or (i_s >= 'A' and i_s <= 'Z') or (i_s >= '0' and i_s <= '9'):
                s1 += i_s

        for i_s in s[::-1]:
            if (i_s >= 'a' and i_s <= 'z') or (i_s >= 'A' and i_s <= 'Z') or (i_s >= '0' and i_s <= '9'):
                s2 += i_s

        if s1.lower() == s2.lower():
            return True
        else:
            return False

a = Solution()
result = a.isPalindrome("A man, a plan, a canal: Panama")
print(result)