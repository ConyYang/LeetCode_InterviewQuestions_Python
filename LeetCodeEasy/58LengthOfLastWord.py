class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        local_count = 0
        global_count = 0
        for i_s in s:
            if i_s != ' ':
                local_count += 1
                global_count = local_count
            else:
                local_count = 0
        return global_count


a = Solution()
length = a.lengthOfLastWord("Hello World")
print(length)