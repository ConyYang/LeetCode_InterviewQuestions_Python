class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        compare_str = ""
        for word in wordDict:
            compare_str += word
        print(compare_str)
        length = len(compare_str)
        print(length)
        for i in range(len(s)):
            if s[i] == compare_str[0]:
                print(s[i])
                if s[i:i + length] == compare_str:
                    print(s[i:i+length])
                    return True
        return False

a = Solution()
s = "a"
wordDict = ["a"]
result = a.wordBreak(s, wordDict)
print(result)