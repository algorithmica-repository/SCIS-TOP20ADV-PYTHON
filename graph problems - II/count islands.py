import sys
import graphutils as utils
from queue import Queue
from disjointset2 import UnionbySizePathCompressionDisjointSet

def auxDfs(u, v, visit, inp):
    if(u < 0 or u >= len(inp) or v < 0 or v >= len(inp[0]) or inp[u][v]==0 or visit[u][v]== 1):
        return
    visit[u][v] = 1
    auxDfs(u+1, v, visit, inp)
    auxDfs(u-1, v, visit, inp)
    auxDfs(u, v-1, visit, inp)
    auxDfs(u, v+1, visit, inp)

#TC:Theta(mn)   SC:Theta(mn)
def countIslands1(inp):
    m = len(inp)
    n = len(inp[0])
    nislands = 0
    visit = [ [0] * n for i in range(m)]
    #print(visit)
    for u in range(m):
        for v in range(n):
            if(inp[u][v] == 1 and visit[u][v] == 0):
                auxDfs(u, v, visit, inp)
                nislands += 1
                #print(visit)
    return nislands
#-----------------------------------------
    
def isValid(x, y, inp, visit):
    if(x < 0 or x >= len(inp) or y < 0 or y >= len(inp[0]) or inp[x][y]==0 or visit[x][y]== 1):
        return False
    return True

def auxBfs(u, v, visit, inp):
    q = Queue()
    q.put((u,v))
    visit[u][v] = 1
    
    while(not q.empty()):
        p = q.get()
        
        if(isValid(p[0]-1, p[1], inp, visit)):
            visit[p[0]-1][p[1]] = 1
            q.put((p[0]-1, p[1]))
            
        if(isValid(p[0]+1, p[1], inp, visit)):
            visit[p[0]+1][p[1]] = 1
            q.put((p[0]+1, p[1]))
            
        if(isValid(p[0], p[1]-1, inp, visit)):
            visit[p[0]][p[1]-1] = 1
            q.put((p[0], p[1]-1))
            
        if(isValid(p[0], p[1]+1, inp, visit)):
            visit[p[0]][p[1]+1] = 1
            q.put((p[0], p[1]+1))
            
#TC:Theta(mn)   SC:Theta(mn)
def countIslands2(inp):
    m = len(inp)
    n = len(inp[0])
    nislands = 0
    visit = [ [0] * n for i in range(m)]
    #print(visit)
    for u in range(m):
        for v in range(n):
            if(inp[u][v] == 1 and visit[u][v] == 0):
                auxBfs(u, v, visit, inp)
                nislands += 1
                #print(visit)
    return nislands
#-----------------------------------------
def auxUnion(i, j, x, y, inp, set):
    if(x < 0 or x >= len(inp) or y < 0 or y >= len(inp[0]) or inp[x][y]==0):
        return
    n = len(inp[0])
    set.union(i*n+j, x*n+y)
   
#TC:Theta(mn)   SC:Theta(mn)
def countIslands3(inp):
    m = len(inp)
    n = len(inp[0])
    nzeros = 0
    set = UnionbySizePathCompressionDisjointSet(m*n)
    for u in range(m):
        for v in range(n):
            if(inp[u][v] == 1):
                auxUnion(u, v, u-1, v, inp, set)
                auxUnion(u, v, u, v+1, inp, set)
            else:
                nzeros += 1
    return set.size() - nzeros
#-----------------------------------------
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])    
    inp = utils.randomGrid(m, n, m+n)
    utils.display(inp)
    print(countIslands1(inp))
    print(countIslands2(inp))
    print(countIslands3(inp))
    
if __name__=="__main__":
    main()
