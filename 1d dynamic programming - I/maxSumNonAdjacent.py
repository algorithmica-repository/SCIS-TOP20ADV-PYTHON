import sys
import random

class MyInteger():
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def set(self, val):
        self.val = val
        
def auxMaxSum1(i, psum, gmax, inp):
    if(i >= len(inp)):
        gmax.set(max(gmax.get(), psum))
        return
    auxMaxSum1(i+2, psum+inp[i], gmax, inp)
    auxMaxSum1(i+1, psum, gmax, inp)

#TC:Theta(2 ^ n)  SC:Theta(n)
def maxSum1(inp):
    gmax = MyInteger(-sys.maxsize-1)
    auxMaxSum1(0, 0, gmax, inp)
    return gmax.get()
    
#--------------------------------------
def auxMaxSum2(i, inp):
    if(i >= len(inp)):
        return 0
    inclusive = auxMaxSum2(i+2, inp) + inp[i]
    exclusive = auxMaxSum2(i+1, inp)
    return max(inclusive, exclusive)

#TC:Theta(2 ^ n)  SC:Theta(n)
def maxSum2(inp):
    return auxMaxSum2(0, inp)

#-----------------------------------
def auxMaxSum3(i, mem, inp):
    if(i >= len(inp)):
        return 0
    if(mem[i] != 0):
        return mem[i]
    inclusive = auxMaxSum3(i+2, mem, inp) + inp[i]
    exclusive = auxMaxSum3(i+1, mem, inp)
    mem[i] = max(inclusive, exclusive)
    return mem[i]

#TC:Theta(n)  SC:Theta(n)
def maxSum3(inp):
    mem = [0]*len(inp)
    return auxMaxSum3(0, mem, inp)

#----------------------------------------

#TC:Theta(n)  SC:Theta(n)
def maxSum4(inp):
    mem = [0]*(len(inp)+2)
    mem[len(inp)] = mem[len(inp)+1] = 0
    for i in range(len(inp)-1, -1, -1):
        inclusive = mem[i+2] + inp[i]
        exclusive = mem[i+1]
        mem[i] = max(inclusive, exclusive)
    traceOptimalRoute(mem, inp)        
    return mem[0]

def traceOptimalRoute(mem, inp):
    print(mem)
    i = 0
    while(i < len(inp)):
        if(mem[i] == mem[i+1]):
            i = i + 1
        else:
            print(inp[i], end=",")
            i = i + 2
    print()
 
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(0, n)
    print(inp)
    #print(maxSum1(inp))
    #print(maxSum2(inp))
    #print(maxSum3(inp))
    print(maxSum4(inp))
    
if __name__=="__main__":
    main()
