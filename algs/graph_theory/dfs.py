# when you do it recrusively u need a wrapper
# runtime: O(n + m)
def DFSWrapper(G, s):
    parents = {}
    times = {}

    count = [0]

    # OPTIONAL to ignore bad source node
    # parents[s] = None
    # for s in G:
    #   if s not in parents:
    #       dfs(G, s, times, parents, count)

    parents[s] = None
    dfs(G, s, times, parents, count)

    return parents, times


def dfs(G, u, times, parents, count):
    count[0] += 1
    times[u] = [count[0], None]

    for v in G[u]:
        if v not in parents:
            # optional to quit if its a cycle
            # if v in times and times[v][1] == None:
            #     return
            parents[v] = u
            dfs(G, v, times, parents, count)

    count[0] += 1
    times[u][1] = count[0]


G = {
    "s": {"b": "", "c": ""},
    "b": {"s": "", "c": "", "h": "", "i": ""},
    "c": {"s": "", "b": "", "i": "", "d": "", "g": ""},
    "h": {"b": "", "i": "", "e": ""},
    "i": {"b": "", "c": "", "h": ""},
    "e": {"h": "", "d": ""},
    "d": {"e": "", "c": "", "f": ""},
    "f": {"d": "", "c": "", "g": ""},
    "g": {"c": "", "f": ""}
}

p, d = DFSWrapper(G, "s")
print(p)
print(d)
