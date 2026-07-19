def build_adj_list(n, edges):
    
    # Create an empty list for every vertex
    graph = [[] for _ in range(n)]

    # Add edges
    for u, v in edges:
        graph[u].append(v)
        # graph[v].append(u)   # Uncomment for an undirected graph

    return graph


n = 5

edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4)
]

graph = build_adj_list(n, edges)

for i in range(n):
    print(i, "->", graph[i])