# Graph Theory

A network of nodes and edges.

Some are directed, others aren't.

For these algorithms, I use an adjacency list using nested hash tables.

This is useful for accessing items in constant time.

So, we have:
- BFS
  - search all nodes in layers
  - minimum edges to all other nodes from source
  - can be used to find connected components
- DFS
  - can be used to find topological order of directed graph
  - can be used to find connected components
  - determine if DAG
- Zero Indegree
  - another way to determine if DAG/get topological ordering
- Dijkstra
  - find the shortest paths of directed graph with nonnegative weights
- MST
  - find shortest paths of all nodes to all other nodes in the graph
