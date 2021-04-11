import sys
import graphutils as utils
import random

def auxDfs(u, t, visit, inp, path):
    if(u == t):
        print(path)
        return
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v] == 1 and visit[v]==0):
            auxDfs(v, t, visit, inp, path + str(v) + "->")
    visit[u] = 0
            
#TC:Theta(V^V)   SC:Theta(V)
def allRoutes(inp, s, t):
    n = len(inp)
    visit = [0] * n
    auxDfs(s, t, visit, inp, str(s) + "->")

def main():
    n = int(sys.argv[1])
    inp = utils.completeGraph(n)
    utils.display(inp)
    s = random.randint(0, n-1)
    t = random.randint(0, n-1)
    print(s, t)
    allRoutes(inp, s, t)
    
if __name__=="__main__":
    main()
