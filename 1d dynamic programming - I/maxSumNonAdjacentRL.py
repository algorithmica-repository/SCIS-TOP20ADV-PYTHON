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
    if(i < 0):
        gmax.set(max(gmax.get(), psum))
        return
    auxMaxSum1(i-2, psum+inp[i], gmax, inp)
    auxMaxSum1(i-1, psum, gmax, inp)

#TC:Theta(2 ^ n)  SC:Theta(n)
def maxSum1(inp):
    gmax = MyInteger(-sys.maxsize-1)
    auxMaxSum1(len(inp)-1, 0, gmax, inp)
    return gmax.get()
    
#--------------------------------------
def auxMaxSum2(i, inp):
    if(i < 0):
        return 0
    inclusive = auxMaxSum2(i-2, inp) + inp[i]
    exclusive = auxMaxSum2(i-1, inp)
    return max(inclusive, exclusive)

#TC:Theta(2 ^ n)  SC:Theta(n)
def maxSum2(inp):
    return auxMaxSum2(len(inp)-1, inp)

#-----------------------------------
def auxMaxSum3(i, mem, inp):
    if(i < 0):
        return 0
    if(mem[i] != 0):
        return mem[i]
    inclusive = auxMaxSum3(i-2, mem, inp) + inp[i]
    exclusive = auxMaxSum3(i-1, mem, inp)
    mem[i] = max(inclusive, exclusive)
    return mem[i]

#TC:Theta(n)  SC:Theta(n)
def maxSum3(inp):
    mem = [0]*len(inp)
    return auxMaxSum3(len(inp)-1, mem, inp)

#----------------------------------------

#TC:Theta(n)  SC:Theta(n)
def maxSum4(inp):
    mem = [0]*(len(inp)+2)
    mem[0] = mem[1] = 0
    for i in range(2, len(mem)):
        inclusive = mem[i-2] + inp[i-2]
        exclusive = mem[i-1]
        mem[i] = max(inclusive, exclusive)
    traceOptimalRoute(len(mem)-1, mem, inp)  
    print()
    return mem[-1]

def traceOptimalRoute(i, mem, inp):
    if(i <= 1):
        return
    if(mem[i] == mem[i-1]):
        traceOptimalRoute(i-1, mem, inp)
    else:
        traceOptimalRoute(i-2, mem, inp)
        print(inp[i-2], end=",")

#----------------------------------------
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
