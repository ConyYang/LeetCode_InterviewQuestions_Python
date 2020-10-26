class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        max_len = max(l1, l2)

        for i in range(max_len):
            if i < l1:
                w1 = int(v1[i])
            else:
                w1 = 0
            if i < l2:
                w2 = int(v2[i])
            else:
                w2 = 0
            if w1 > w2:
                return 1
            elif w1 < w2:
                return -1
        return 0


a = Solution()
result = a.compareVersion("1.01", "1.001")
print(result)