from collections import defaultdict

def is_valid_tree(n, edges):
    # Condition 1: A tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    # Build adjacency list
    graph = defaultdict(list)

    for i in range(n):
        graph[i]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Condition 2: Check if graph is connected
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)

    return len(visited) == n

n = 5
edges = [(0,1), (0,2), (1,3), (1,4)]

print(is_valid_tree(n, edges))