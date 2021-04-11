import sys
import random

#TC:theta(n)   SC:Theta(n)
def maxSubarraySum(inp):
    mem = [0] * (len(inp) + 1)
    mem[-1] = 0
    pos = len(inp)
    gmax = -sys.maxsize-1
    for i in range(len(inp)-1, -1, -1):
        mem[i] = max(inp[i], inp[i] + mem[i+1])
        #gmax = max(gmax, mem[i])
        if(mem[i] > gmax):
            gmax = mem[i]
            pos = i
    print(pos)
    return gmax

#TC:theta(n)   SC:O(1)
def maxSubarraySumOpt(inp):
    res = 0
    pos = len(inp)
    gmax = -sys.maxsize-1
    for i in range(len(inp)-1, -1, -1):
        res = max(inp[i], inp[i] + res)
        if(res > gmax):
            gmax = res
            pos = i
    print(pos)
    return gmax

def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, n)
        if(random.randint(0,1) == 0):
            inp[i] *= -1
    print(inp)
    print(maxSubarraySum(inp))
    print(maxSubarraySumOpt(inp))
    
if __name__=="__main__":
    main()
