from collections import defaultdict

def adjList(n, edges):
    graph = defaultdict(list)

    for i in range(n):
        graph[i]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph

graph = adjList(n, edges)

print(graph)

# Later
bfs(graph, 0)
dfs(graph, 0)