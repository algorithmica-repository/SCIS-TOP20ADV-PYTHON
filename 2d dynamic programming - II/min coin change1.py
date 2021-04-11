import sys

def traceOptimalRoute(inp, mem):
    i = len(mem)-1
    while(i > 0):
        for j in range(len(inp)):
            if(inp[j] <= i):
                if(mem[i-inp[j]] + 1 == mem[i]):
                    print(inp[j], end='+')
                    i = i - inp[j]
                    break
    print()
    
#TC:Theta(nS)  SC:Theta(S)
def minCoinChange(inp, s):
    mem = [0]*(s+1)
    mem[0] = 0
    
    for i in range(1, s+1):
        mn = sys.maxsize
        for j in range(len(inp)):
            if(inp[j] <= i):
                mn = min(mn, mem[i-inp[j]] + 1)
        mem[i] = mn
    print(mem)
    traceOptimalRoute(inp, mem)
    return mem[-1]

def main():
    inp = [1, 3, 4]
    s = 15
    print(inp)
    print(s)
    print(minCoinChange(inp, s))
    
if __name__=="__main__":
    main()
