from collections import defaultdict

def adjList(n, edges):
    graph = defaultdict(list)

    for i in range(n):
        graph[i]

    for u, v , w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))

    return graph

n = 4
edges = [
    (0, 1, 5),
    (1, 2, 3),
    (2, 3, 8)
]

graph = adjList(n, edges)

print(graph)

