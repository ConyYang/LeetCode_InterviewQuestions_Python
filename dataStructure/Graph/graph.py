class Graph(object):
    def __init__(self):
        self.nodes = []  # set of nodes
        self.edge = {}  # set of edges

    def insert(self, a, b):
        # if a is not in nodes set, add a
        if a not in self.nodes:
            self.nodes.append(a)
            self.edge[a] = list()
        # if b is not in nodes set, add b
        if b not in self.nodes:
            self.nodes.append(b)
            self.edge[b] = list()
        # a connect b
        self.edge[a].append(b)
        # b connect a
        self.edge[b].append(a)

    def succ(self, a):
        # return nodes connect with a
        return self.edge[a]

    def show_nodes(self):
        # return nodes set of graph
        return self.nodes

    def show_edge(self):
        print(self.edge)


graph = Graph()
graph.insert('0', '1')
graph.insert('0', '2')
graph.insert('0', '3')
graph.insert('1', '3')
graph.insert('2', '3')
graph.show_edge()