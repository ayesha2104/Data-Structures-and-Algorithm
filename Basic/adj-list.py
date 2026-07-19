from collections import defaultdict

def adjList(n,edges):
    
    graph=defaultdict(list)
    #Undirected,unweighted
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    print(graph)

edges=[(1,0),(0,2),(2,3),(3,1)]
n=4

adjList(n,edges)
