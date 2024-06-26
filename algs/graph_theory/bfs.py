# raw run of bfs
# runtime: O(n + m)
def bfs_raw(G, s):
    parents = {}
    parents[s] = None

    dist = {}
    dist[s] = 0

    q = []
    q.append(s)

    while q:
        u = q.pop(0)
        for v in G[u]:
            if v not in parents:
                parents[v] = u
                dist[v] = dist[u] + 1
                q.append(v)

    return parents, dist


# undirected, unweighted graph
G = {
    "s": {"b": "", "c": ""},
    "b": {"s": "", "c": "", "h": "", "i": ""},
    "c": {"s": "", "b": "", "i": "", "d": "", "g": "", "f": "", "h": ""},
    "h": {"b": "", "e": ""},
    "i": {"b": "", "c": ""},
    "e": {"h": "", "d": ""},
    "d": {"e": "", "c": "", "f": ""},
    "f": {"d": "", "c": "", "g": ""},
    "g": {"c": "", "f": ""}
}

p, d = bfs_raw(G, "s")
print(p)
print(d)

# variants to solve problems


def count_components(G):
    visited = set()
    count = 0
    for v in G:
        if v not in visited:
            visited.add(v)
            component = bfs_get_connected(v, visited, G)
            count += 1
            # do something with component

    return count


def bfs_get_connected(start, visited, graph):
    q = [start]
    connected = []

    while q:
        v = q.pop(0)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
        connected.append(v)

    return connected
