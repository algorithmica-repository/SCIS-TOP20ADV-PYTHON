import sys
import random

class MyInteger():
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def set(self, val):
        self.val = val
        
def auxMaxCoins1(i, j, psum, gmax, inp):
    if(i >= len(inp) or j >= len(inp)):
        return
    if(i == len(inp)-1 and j == len(inp)-1):
        gmax.set(max(gmax.get(), psum+inp[i][j]))
        return    
    auxMaxCoins1(i+1, j, psum + inp[i][j], gmax, inp)
    auxMaxCoins1(i, j+1, psum + inp[i][j], gmax, inp)
    
#TC:theta(2^2n)   SC:Theta(n)
def maxCoins1(inp):
    gmax = MyInteger(0)
    auxMaxCoins1(0, 0, 0, gmax, inp)
    return gmax.get()
#---------------------------------------------------
def auxMaxCoins2(i, j, inp):
    if(i >= len(inp) or j >= len(inp)):
        return 0  
    bsum = auxMaxCoins2(i+1, j, inp)
    rsum = auxMaxCoins2(i, j+1, inp)
    return max(bsum, rsum) + inp[i][j]
    
#TC:theta(2^2n)   SC:Theta(n)
def maxCoins2(inp):
    return auxMaxCoins2(0, 0, inp)
#---------------------------------------------------
def auxMaxCoins3(i, j, mem, inp):
    if(i >= len(inp) or j >= len(inp)):
        return 0 
    if(mem[i][j] != 0):
        return mem[i][j]
    bsum = auxMaxCoins3(i+1, j, mem, inp)
    rsum = auxMaxCoins3(i, j+1, mem, inp)
    mem[i][j] =  max(bsum, rsum) + inp[i][j]
    return mem[i][j]
    
#TC:theta(n^2)   SC:Theta(n^2)
def maxCoins3(inp):
    mem = [ [0]*len(inp) for i in range(len(inp))]
    return auxMaxCoins3(0, 0, mem, inp)
#---------------------------------------------------
#TC:theta(n^2)   SC:Theta(n^2)
def maxCoins4(inp):
    n = len(inp)
    mem = [ [0]*(n+1) for i in range(n+1)]
    for i in range(n):
        mem[n][i] = 0
        mem[i][n] = 0
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            bsum = mem[i+1][j]
            rsum = mem[i][j+1]
            mem[i][j] =  max(bsum, rsum) + inp[i][j] 
    traceOptimalRoute(mem, inp)
    return mem[0][0]

def traceOptimalRoute(mem, inp):
    i = 0
    j = 0
    while(i < len(inp) and j < len(inp)):
        print(inp[i][j], end=",")
        if(mem[i+1][j] > mem[i][j+1]):
            i = i + 1
        else:
            j = j + 1
    print()
#---------------------------------------------------
def main():
    n = int(sys.argv[1])
    inp = [ [0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            inp[i][j] = random.randint(1, n)
    print(inp)
    #print(maxCoins1(inp))
    #print(maxCoins2(inp))
    #print(maxCoins3(inp))
    print(maxCoins4(inp))
    
if __name__=="__main__":
    main()
