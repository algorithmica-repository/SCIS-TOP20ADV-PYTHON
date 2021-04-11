import sys
import random

class MyInteger():
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def set(self, val):
        self.val = val
        
def auxKnapsack1(start, m, csum, inp, gmax):
    if(m < 0):
        return
    gmax.set(max(gmax.get(), csum))
    for i in range(start, len(inp)):
        if(inp[i] <= m):
            auxKnapsack1(i+1, m-inp[i], csum+inp[i], inp, gmax)

#TC:O(2^n)  SC:O(n)
def knapsack1(inp, m):
    gmax = MyInteger(0)
    auxKnapsack1(0, m, 0, inp, gmax) 
    return gmax.get()
#-----------------------------------------------
def traceOptimalRoute(inp, mem):
    i = len(mem)-1
    j = 0
    while(i > 0 and j < len(inp)):
            if(inp[j] > i):
                j += 1
            else:
                inclusive = mem[i-inp[j]][j+1] + inp[j]
                exclusive = mem[i][j+1]
                if(inclusive > exclusive):
                    print(inp[j], end="+")
                    i = i - inp[j]
                    j += 1
                else:
                    j += 1
    print()
    
#TC:Theta(nm)  SC:Theta(nm)
def knapsack3(inp, m):
    n = len(inp)
    mem = [ [0]*(n+1) for i in range(m+1)]
    
    for j in range(0, n+1):
        mem[0][j] = 0
    for i in range(1, m+1):
        mem[i][n] = 0
    
    for i in range(1, m+1):
        for j in range(n-1, -1, -1):
            if(inp[j] > i):
                mem[i][j] = mem[i][j+1]
            else:
                inclusive = mem[i-inp[j]][j+1] + inp[j]
                exclusive = mem[i][j+1]
                mem[i][j] = max(inclusive, exclusive)
    print(mem)
    traceOptimalRoute(inp, mem)
    return mem[m][0]

    
#------------------------------------------------
def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, 2*n)
    print(inp)
    print(m)
    print(knapsack1(inp, m))
    print(knapsack3(inp, m))
    
if __name__=="__main__":
    main()
