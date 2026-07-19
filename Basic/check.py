def detect_graph_type(n, edges):
    # Create adjacency matrix
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Assume edges are given as they are
    for u, v in edges:
        matrix[u][v] = 1

    # Check symmetry
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return "Directed"

    return "Undirected"

n = 4
edges = [(0,1), (1,2), (2,3)]

print(detect_graph_type(n, edges))