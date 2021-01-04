def CalculateRoad(town_count, road_count, road):
    # Write your code here
    # use graph to do?
    # save nodes to a list
    # nodes = list(i for i in range(town_count))
    # edges = dict.fromkeys(nodes, [])

    # # save the number of existing edges
    # # [[0,1], [1,2]]

    for line in road:
        nodes, edge = insert(line[0], line[1])
    print(nodes)
    print(edge)


def insert(x, y):
    nodes = []
    edge = {}
    if x not in nodes:
        nodes.append(x)
        edge[x] = list()
    if y not in nodes:
        nodes.append(y)
        edge[y] = list()
    edge[x].append(y)
    edge[y].append(x)
    return nodes, edge


if __name__ == '__main__':
    CalculateRoad(4, 2, [[0,1], [1,2]])