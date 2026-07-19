
from collections import defaultdict

def build_adj_list(n, edges):
    graph = defaultdict(list)

    # Ensure all vertices exist
    for i in range(n):
        graph[i]

    # Add every edge exactly as given
    for u, v in edges:
        graph[u].append(v)

    return graph


n = 4

edges = [
    (0, 1),
    (0, 1),   # Duplicate edge
    (1, 2),
    (2, 2),   # Self-loop
    (2, 3),
    (3, 3),   # Self-loop
    (3, 3)    # Duplicate self-loop
]

graph = build_adj_list(n, edges)

for node in graph:
    print(f"{node} -> {graph[node]}")