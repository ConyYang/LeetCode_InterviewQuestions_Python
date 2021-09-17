class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (len(str1) < len(str2)): return self.gcdOfStrings(str2, str1)
        if (len(str2) == 0): return str1
        if (str1[0:len(str2)] != str2): return ""
        return self.gcdOfStrings(str1[len(str2):], str2)