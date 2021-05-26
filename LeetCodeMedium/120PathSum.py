class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)
        f = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n + 1):
            for j in range(1, i+1):
                f[i][j] = triangle[i-1][j-1]
                if i == 1 and j == 1: continue
                if j == 1:
                    f[i][j] += f[i - 1][j]
                elif j == i:
                    f[i][j] += f[i - 1][j - 1]
                else:
                    f[i][j] += min(f[i - 1][j], f[i - 1][j - 1])
        return min(f[n])


if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    a = Solution()
    f = a.minimumTotal(tri)
    print(f)
