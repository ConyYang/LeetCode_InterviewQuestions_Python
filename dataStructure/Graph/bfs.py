def bfs(graph, start):
    # explored: nodes already traversed
    explored = []
    # queue: queue of nodes waited to be traversed
    queue = [start]

    while queue:
        # v: a nodes to be traversed
        v = queue.pop(0)
        # w: neighbors of v
        for w in graph[v]:
            # if w is not explored, then traverse it
            if w not in explored:
                # add w to explored list
                explored.append(w)
                # add w to queue of nodes wait to be traversed
                queue.append(w)
    return explored


G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(bfs(G, '0'))