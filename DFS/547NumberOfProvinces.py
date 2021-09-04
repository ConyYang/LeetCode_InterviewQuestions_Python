class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for i in range(len(isConnected))]
        numProvinces = 0

        for i in range(len(isConnected)):
            if not (visited[i]):
                numProvinces += 1
                self.DFS(isConnected, visited, i)

        return numProvinces

    def DFS(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.DFS(isConnected, visited, j)