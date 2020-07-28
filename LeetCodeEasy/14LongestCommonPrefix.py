class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        cur_str = strs[0]
        common_str = ""
        for i in range(1, len(strs)):
            next_str = strs[i]
            k = 0
            for s in cur_str:
                try:
                    if s == next_str[k]:
                        common_str += s
                    else:
                        break
                    k += 1
                except:
                    pass
            cur_str = common_str
            common_str = ""
        return cur_str


a =Solution()
cur = a.longestCommonPrefix(["dog","racecar","car"])
print(cur)