import sys

def traceOptimalRoute(inp, mem):
    i = len(mem)-1
    j = 0
    while(i > 0 and j < len(inp)):
            if(inp[j] > i):
                j += 1
            else:
                inclusive = mem[i-inp[j]][j] + 1
                exclusive = mem[i][j+1]
                if(inclusive < exclusive):
                    print(inp[j], end="+")
                    i = i - inp[j]
                else:
                    j += 1
    print()
    
#TC:Theta(nS)  SC:Theta(nS)
def minCoinChange(inp, s):
    n = len(inp)
    mem = [ [0]*(n+1) for i in range(s+1)]
    
    for j in range(0, n+1):
        mem[0][j] = 0
    for i in range(1, s+1):
        mem[i][n] = sys.maxsize
    
    for i in range(1, s+1):
        for j in range(n-1, -1, -1):
            if(inp[j] > i):
                mem[i][j] = mem[i][j+1]
            else:
                inclusive = mem[i-inp[j]][j] + 1
                exclusive = mem[i][j+1]
                mem[i][j] = min(inclusive, exclusive)
    print(mem)
    traceOptimalRoute(inp, mem)
    return mem[s][0]

def main():
    inp = [1, 3, 4]
    s = 15
    print(inp)
    print(s)
    print(minCoinChange(inp, s))
    
if __name__=="__main__":
    main()
