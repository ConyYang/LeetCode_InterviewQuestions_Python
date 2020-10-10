# DFS search


def dfs(G, s, S=None, res=None):
    """
    :param G: G is the graph
    :param s: the start node we visit
    :param S: Save nodes already visited; A set
    :param res: Save the traverse order; An array
    :return:
    """
    if S is None:
        S = set()
    if res is None:
        res = []
    res.append(s)
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        S.add(u)
        dfs(G, u, S, res)

    return res


G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(dfs(G, '0'))