import sys
import graphutils as utils
from queue import Queue
from disjointset2 import UnionbySizePathCompressionDisjointSet

def auxDfs(u, visit, inp):
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v] == 1 and visit[v]==0):
            auxDfs(v, visit, inp)
            
#TC:Theta(V^2)   SC:Theta(V)
def countCircles1(inp):
    n = len(inp)
    ncircles = 0
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            auxDfs(u, visit, inp)
            ncircles += 1
    return ncircles
#-----------------------------------------
def auxBfs(u, visit, inp):
    q = Queue()
    q.put(u)
    visit[u] = 1
    
    while(not q.empty()):
        u = q.get()
        for v in range(len(inp)):
            if(inp[u][v] == 1 and visit[v]==0):
                q.put(v)
                visit[v]= 1
            
#TC:Theta(V^2)   SC:Theta(V)
def countCircles2(inp):
    n = len(inp)
    ncircles = 0
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            auxBfs(u, visit, inp)
            ncircles += 1
    return ncircles
#-----------------------------------------
#TC:Theta(V^2)   SC:Theta(V)
def countCircles3(inp):
    n = len(inp)
    set = UnionbySizePathCompressionDisjointSet(n)
    for u in range(n):
        for v in range(n):
            if(inp[u][v] == 1):
                set.union(u, v)
    return set.size()
#-----------------------------------------
def main():
    n = int(sys.argv[1])
    inp = utils.randomUndirectedGraph(n)
    utils.display(inp)
    print(countCircles1(inp))
    print(countCircles2(inp))
    print(countCircles3(inp))
    
if __name__=="__main__":
    main()
