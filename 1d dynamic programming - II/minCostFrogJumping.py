import sys
import random

def traceOptimalRoute(mem, inp):
    i = 0
    while(i < len(inp)):
        print(inp[i], end=",")
        if(mem[i] == mem[i+1] + inp[i]):
            i = i + 1
        else:
            i = i + 2
    print()
    
def minCostJump(inp):
    mem = [0]*(len(inp)+1)
    mem[-1] = 0
    mem[-2] = inp[-1]
    for i in range(len(mem)-3, -1, -1):
        mem[i] = min(mem[i+1], mem[i+2]) + inp[i]
    traceOptimalRoute(mem, inp)
    return mem[0]

def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, n)
    print(inp)
    print(minCostJump(inp))
    
if __name__=="__main__":
    main()
