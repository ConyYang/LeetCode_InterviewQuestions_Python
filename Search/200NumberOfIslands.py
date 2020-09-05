class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_len = len(grid)
        if row_len == 0:
            return 0
        col_len = len(grid[0])

        result = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '1':
                    result += 1
                    self._dfs(grid, row, col, row_len, col_len)
        return result

    def _dfs(self, grid, row, col, row_len, col_len):
        if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self._dfs(grid, row, col - 1, row_len, col_len)
        self._dfs(grid, row, col + 1, row_len, col_len)
        self._dfs(grid, row - 1, col, row_len, col_len)
        self._dfs(grid, row + 1, col, row_len, col_len)


a = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = a.numIslands(grid)
print(result)