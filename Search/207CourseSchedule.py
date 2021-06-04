class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for p in prerequisites:
            if p[0] not in graph.keys():
                graph[p[0]] = []
                graph[p[0]].append(p[1])
            else:
                graph[p[0]].append(p[1])

        """ States: 0- Unknown 1- visiting 2- visited
        """

        states = [0 for _ in range (numCourses)]

        for i in range(numCourses):
            if self.dfs(i, states, graph): return False

        return True


    def dfs(self, cur, states, graph):
        if states[cur] == 1: return True # cycle
        if states[cur] == 2: return False # no cycle

        states[cur] = 1

        if cur in graph:
            for j in graph[cur]:
                if self.dfs(j, states, graph):
                    return True

        states[cur] = 2

        return False



if __name__ == '__main__':
    a = Solution()
    print(a.canFinish(2, [[1, 0]]))

