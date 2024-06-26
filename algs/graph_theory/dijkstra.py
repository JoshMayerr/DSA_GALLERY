from heapq import heapify, heappop, heappush
import math

# Runtime: O(mlogn)


def dijkstra(G, s):
    distances = {v: math.inf for v in G}
    distances[s] = 0
    parents = {s: None}

    visited = set()

    pq = [(0, s)]
    heapify(pq)

    while pq:
        curr_dist, u = heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for v in G[u]:
            tentative_distance = curr_dist + G[u][v]
            if tentative_distance < distances[v]:
                distances[v] = tentative_distance
                heappush(pq, (tentative_distance, v))
                parents[v] = u

    return distances, parents


G = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
distances, parents = dijkstra(G, 'A')
print("Distances:", distances)
print("Parents:", parents)
