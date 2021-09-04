class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie = 0
        child = 0
        while (cookie < len(s)) and (child < len(g)):
            if (g[child] <= s[cookie]):
                child += 1
            cookie += 1

        return child