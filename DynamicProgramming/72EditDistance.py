class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if s1[i] == s2[j]:
        #     啥都别做（skip）
        #     i, j 同时向前移动
        # else:
        #     三选一：
        #         插入（insert）table(i, j - 1) + 1,    # 插入
        #         删除（delete）table(i - 1, j) + 1,    # 删除
        #         替换（replace）table(i - 1, j - 1) + 1 # 替换

        m = len(word1) + 1
        n = len(word2) + 1

        table = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            table[i][0] = i
        for j in range(n):
            table[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                # state transfer function
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(table[i - 1][j] + 1,
                                      table[i][j - 1] + 1,
                                      table[i - 1][j - 1] + 1)
        return table[m - 1][n - 1]