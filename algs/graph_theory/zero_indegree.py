# find the topological sort with the zero indegree alg
def zero_indegree(G, n):
    indegree = [0] * n

    # calculate the indegree of every node
    for i in range(n):
        for v in G[i]:
            indegree[v] += 1

    q = []
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        u = q.pop(0)
        result.append(u)
        for v in G[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(result) != n:
        return []
    else:
        return result
