import sys
import graphutils as utils
from queue import Queue
from disjointset2 import UnionbySizePathCompressionDisjointSet

def auxDfs(u, parent, visit, inp):
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v] == 1):
            if(visit[v]==0): #forward edge
                if(auxDfs(v, u, visit, inp)):
                    return True
            else: #back edge
                if(v != parent):
                    return True
    return False
            
#TC:Theta(V^2)   SC:Theta(V)
def detectCycle1(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(auxDfs(u, u, visit, inp)):
                return True
    return False
#-----------------------------------------
def auxBfs(u, visit, inp):
    q = Queue()
    q.put(u)
    visit[u] = 1
    
    while(not q.empty()):
        u = q.get()
        visit[u] = 2
        for v in range(len(inp)):
            if(inp[u][v] == 1):
                if(visit[v]==0):
                    q.put(v)
                    visit[v]= 1
                else:
                    if(visit[v] == 1):
                        return True
    return False
                
#TC:Theta(V^2)   SC:Theta(V)
def detectCycle2(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(auxBfs(u, visit, inp)):
                return True
    return False
#-----------------------------------------
#TC:Theta(V^2)   SC:Theta(V)
def detectCycle3(inp):
    n = len(inp)
    set1 = UnionbySizePathCompressionDisjointSet(n)
    for u in range(n):
        for v in range(u+1, n):
            if(inp[u][v] == 1):
                if(set1.find(u) == set1.find(v)):
                    return True
                set1.union(u, v)
    return False
#-----------------------------------------   
def main():
    n = int(sys.argv[1])
    inp = utils.randomUndirectedGraph(n)
    utils.display(inp)
    print(detectCycle1(inp))
    print(detectCycle2(inp))
    print(detectCycle3(inp))
    
if __name__=="__main__":
    main()
