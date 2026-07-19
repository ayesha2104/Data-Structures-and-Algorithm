from collections import defaultdict

def adjList(n, edges):
    graph = defaultdict(list)

    for i in range(n):
        graph[i]

    for u, v in edges:
        graph[u].append(v)

    return graph

n=4
edges=[(0,1),(1,2),(2,3)]
graph = adjList(n, edges)

print(graph)

