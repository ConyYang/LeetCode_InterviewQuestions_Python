class Solution(object):
    def __init__(self):
        self.neighbour = 0

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        total = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    total += 1
                    self.countNeighbour(grid, i, j, m, n)
        return total * 4 - self.neighbour

    def countNeighbour(self, grid, i, j, m, n):
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            self.neighbour += 1
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            self.neighbour += 1
        if i + 1 < m and grid[i + 1][j] == 1:
            self.neighbour += 1
        if j + 1 < n and grid[i][j + 1] == 1:
            self.neighbour += 1