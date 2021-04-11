import sys
import graphutils as utils
from queue import Queue

def displayPartitions(visit):
    print("Partition-1")
    for u in range(len(visit)):
        if(visit[u] == 1):
            print(u, end=' ')
    print()
    print("Partition-2")
    for u in range(len(visit)):
        if(visit[u] == 2):
            print(u, end=' ')
    print()    
    
def auxDfs(u, c, visit, inp):
    visit[u] = c
    for v in range(len(inp)):
        if(inp[u][v] == 1):
            if(visit[v]==0): #forward edge
                if(visit[u] == 1):
                    cc = 2
                else:
                    cc = 1
                if(not auxDfs(v, cc, visit, inp)):
                    return False
            else: #back edge
                if(visit[u] == visit[v]):
                    return False
    return True
            
#TC:Theta(V^2)   SC:Theta(V)
def isBipartite1(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(not auxDfs(u, 1, visit, inp)):
                return False
    displayPartitions(visit)
    return True
#-----------------------------------------
def auxBfs(u, visit, inp):
    q = Queue()
    q.put(u)
    visit[u] = 1
    
    while(not q.empty()):
        u = q.get()
        for v in range(len(inp)):
            if(inp[u][v] == 1):
                if(visit[v]==0):
                    q.put(v)
                    if(visit[u] == 1):
                        visit[v] = 2
                    else:
                        visit[v] = 1
                else:
                    if(visit[v] == visit[u]):
                        return False
    return True
                
#TC:Theta(V^2)   SC:Theta(V)
def isBipartite2(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(not auxBfs(u, visit, inp)):
                return False

    displayPartitions(visit)
    return True
#-----------------------------------------
def main():
    n = int(sys.argv[1])
    inp = utils.randomUndirectedGraph(n)
    utils.display(inp)
    print(isBipartite1(inp))
    print(isBipartite2(inp))
    
if __name__=="__main__":
    main()
