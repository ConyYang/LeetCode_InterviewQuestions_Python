class Solution(object):
    def __init__(self):
        self.graph = {}
        self.visited = []


    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for e in edges:
            u = e[0]
            v = e[1]
            self.visited = []
            if self.hasPath(u, v):
                return e

            if u not in self.graph:
                self.graph[u] = [v]
            else:
                self.graph[u].append(v)

            if v not in self.graph:
                self.graph[v] = [u]
            else:
                self.graph[v].append(u)

        return {}

    def hasPath(self,start, goal):
        if start == goal: return True
        self.visited.append(start)

        if start not in self.graph or goal not in self.graph: return False

        for next in self.graph[start]:
            if next in self.visited: continue
            if self.hasPath(next, goal): return True

        return False


if __name__ == '__main__':
    a = Solution()
    result = a.findRedundantConnection([[1, 2], [1, 3], [2, 3],[4,5]])
    print(result)