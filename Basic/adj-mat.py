


def adjmat(n,edges):

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for u,v in edges:
        mat[u][v]=1

    return mat

n=4
edges=[(0,1),(1,2),(2,3)]

matrix=adjmat(n,edges)

print(matrix)