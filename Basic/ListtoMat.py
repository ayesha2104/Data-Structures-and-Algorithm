def mat(n, adjList):

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in adjList[i]:
            mat[i][j] = 1

    return mat


n = 4
adjList = [
    [1],     
    [2],      
    [3],      
    []        
]

matrix = mat(n, adjList)

for row in matrix:
    print(row)