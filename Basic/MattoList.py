from collections import defaultdict

def lis(n,mat):

    r=len(mat)
    c=len(mat[0])

    adjlist=defaultdict(list)


    for i in range(n):
        adjlist[i]

    for i in range(r):
        for j in range(c):
            if mat[i][j]==1:
                adjlist[i].append(j)   #assuming directed graph
    return adjlist


mat=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
n=len(mat)

resList=lis(n,mat)

print(resList)