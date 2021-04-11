import random

def randomUndirectedGraph(n):
    inp = [ [0]*n for i in range(n)]
    for i in range(n):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if(u != v):
            inp[u][v] = 1
            inp[v][u]= 1
    return inp

def randomGrid(m, n, nedges):
    inp = [ [0]*n for i in range(m)]
    for i in range(nedges):
        u = random.randint(0, m-1)
        v = random.randint(0, n-1)
        inp[u][v] = 1
    return inp

def completeGraph(n):
    inp = [ [0]*n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            inp[i][j] = 1
            inp[j][i]= 1
    return inp

def display(inp):
    n = len(inp)
    for i in range(n):
        for j in range(len(inp[0])):
            print(inp[i][j], end=' ')
        print()
