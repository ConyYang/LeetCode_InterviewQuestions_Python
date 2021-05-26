class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        curr_word = ''
        s += ' '
        dict_compare = {}
        index = 0

        for s_i in s:
            if s_i != ' ':
                curr_word += s_i
            else:
                if curr_word not in dict_compare.keys():
                    if pattern[index] in dict_compare.values():
                        return False
                    dict_compare[curr_word] = pattern[index]
                else:
                    if dict_compare.get(curr_word) != pattern[index]:
                        return False
                index += 1
                curr_word = ''
        if index != len(pattern):
            return False
        return True


s = Solution()
result = s.wordPattern(pattern="abba", s="dog dog dog dog")
print(result)
