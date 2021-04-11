import sys
import graphutils as utils
from queue import Queue
import random

def auxDfs(u, t, visit, inp):
    if(u == t):
        return True
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v] == 1 and visit[v]==0):
            if(auxDfs(v, t, visit, inp)):
                return True
    return False
            
#TC:Theta(V^2)   SC:Theta(V)
def existRoute1(inp, s, t):
    n = len(inp)
    visit = [0] * n
    return auxDfs(s, t, visit, inp)
#-----------------------------------------
def auxBfs(u, t, visit, inp):
    if(u == t):
        return True
    q = Queue()
    q.put(u)
    visit[u] = 1
    
    while(not q.empty()):
        u = q.get()
        for v in range(len(inp)):
            if(inp[u][v] == 1 and visit[v]==0):
                if(v == t):
                    return True
                q.put(v)
                visit[v]= 1
    return False
                
#TC:Theta(V^2)   SC:Theta(V)
def existRoute2(inp, s, t):
    n = len(inp)
    visit = [0] * n
    return auxBfs(s, t, visit, inp)
 #----------------------------------------------           
def main():
    n = int(sys.argv[1])
    inp = utils.randomUndirectedGraph(n)
    utils.display(inp)
    s = random.randint(0, n-1)
    t = random.randint(0, n-1)
    print(s, t)
    print(existRoute1(inp, s, t))
    print(existRoute2(inp, s, t))
    
if __name__=="__main__":
    main()
