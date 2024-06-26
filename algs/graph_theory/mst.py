# there are a few dif algs but im choosing Prim's
import math
from heapq import heappop, heappush, heapify


def prim(G, start):
    mst = {}
    total_cost = 0
    visited = set()

    pq = [(0, start)]
    heapify(pq)

    while pq:
        cost, u = heappop(pq)

        if u in visited:
            continue
        visited.add(u)
        mst[u] = cost
        total_cost += cost

        for v in G[u]:
            if v not in visited:
                heappush(pq, (G[u][v], v))

    return mst, total_cost
