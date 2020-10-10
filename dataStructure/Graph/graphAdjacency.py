# use Adjacency matrix to build graph
"""
The adjacency matrix notation is represented by two arrays,
a one-dimensional array and a two-dimensional array.

A one-dimensional array stores node information,
and a two-dimensional array stores the relationship between nodes.
"""


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex)]

    # For two points that have a connection relationship, set 1 in the matrix to indicate that there is a connection
    # relationship, and if there is no connection relationship, set it to 0
    def insert(self, u, v):
        self.graph[u - 1][v - 1] = 1
        self.graph[v - 1][u - 1] = 1

    def show(self):
        # display the graph
        for i in self.graph:  # row
            for j in i:  # columns
                print(j, end=' ')
            print(' ')


if __name__ == '__main__':
    A = Graph(5)
    edge_set = [[1, 4], [4, 2], [4, 5], [2, 5], [3, 5]]
    for edge in edge_set:
        A.insert(edge[0], edge[1])
    A.show()
