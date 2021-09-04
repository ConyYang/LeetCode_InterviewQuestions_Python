from collections import OrderedDict
from typing import List


def topKFrequent(self, words: List[str], k: int) -> List[str]:
    h = OrderedDict()
    for i in words:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    ls = []
    for i in h:
        ls.append((i, h[i]))
    ls.sort()
    ls = sorted(ls, key=lambda x: x[1], reverse=True)
    fin = []
    for i in range(k):
        fin.append(ls[i][0])
    return fin