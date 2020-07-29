class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        n_len = len(needle)
        for i in range(len(haystack)-n_len+1):
            print(haystack[i:i+n_len])
            if haystack[i:i+n_len] == needle:
                return i
        return -1

a = Solution()
haystack = "a"
needle = "a"
result = a.strStr(haystack, needle)
print(result)