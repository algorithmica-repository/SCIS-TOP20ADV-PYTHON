import sys
import random

class MyInteger():
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def set(self, val):
        self.val = val
        
#TC:O(n* 2^n)  SC:O(1)
def lis1(inp):
    return 0
#--------------------------------------------
def auxLis2(i, plen, gmax, inp):
#    if(i == len(inp)-1):
#        gmax.set(max(gmax.get(), plen+1))
#        return
    for j in range(i+1, len(inp)):
        if(inp[j] > inp[i]):
            auxLis2(j, plen+1, gmax, inp)
    gmax.set(max(gmax.get(), plen+1))
            
#TC:O(n^ n+1)  SC:Theta(n)
def lis2(inp):
    gmax = MyInteger(1)
    for i in range(len(inp)):
        auxLis2(i, 0, gmax, inp)
    return gmax.get()
#-----------------------------------------------
def auxLis3(i, inp):
#    if(i == len(inp)-1):
#        gmax.set(max(gmax.get(), plen+1))
#        return
    mx = 1
    for j in range(i+1, len(inp)):
        if(inp[j] > inp[i]):
            res = auxLis3(j, inp) + 1
            mx = max(res, mx)
    return mx
            
#TC:O(n^ n+1)  SC:Theta(n)
def lis3(inp):
    gmax = 0
    for i in range(len(inp)):
        gmax = max(gmax, auxLis3(i, inp))
    return gmax
#------------------------------------------------------
def auxLis4(i, mem, inp):
#    if(i == len(inp)-1):
#        gmax.set(max(gmax.get(), plen+1))
#        return
    if(mem[i] != 0):
        return mem[i]
    mx = 1
    for j in range(i+1, len(inp)):
        if(inp[j] > inp[i]):
            res = auxLis4(j, mem, inp) + 1
            mx = max(res, mx)
    mem[i] = mx
    return mem[i]
            
#TC:O(n^2)  SC:Theta(n)
def lis4(inp):
    gmax = 0
    mem = [0]*len(inp)
    for i in range(len(inp)):
        gmax = max(gmax, auxLis4(i, mem, inp))
    return gmax
#--------------------------------------------------------
#TC:O(n^2)  SC:Theta(n)
def lis5(inp):
    gmax = 0
    mem = [0]*len(inp)
    mem[len(inp)-1] = 1
    
    for i in range(len(inp)-2, -1, -1):
        mx = 1
        for j in range(i+1, len(inp)):
            if(inp[j] > inp[i]):
                res = mem[j] + 1
                mx = max(res, mx)
        mem[i] = mx 
        if(mem[i] > gmax):
            gmax = mem[i]
            mpos = i
    traceOptimalRoute(mpos, mem, inp)
    print()
    return gmax

def traceOptimalRoute(i, mem, inp):
    while(i < len(inp)):
        print(inp[i], end=",")
        end = True
        for j in range(i+1, len(mem)):
            if(inp[j] > inp[i]):
                end = False
                if(mem[i] == mem[j]+1):
                    i = j
                    break
        if(end):
            break
#---------------------------------------------------
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(0, n)
        #inp[i] = i
    print(inp)
    #print(lis2(inp))
    #print(lis3(inp))
    #print(lis4(inp))
    print(lis5(inp))
    
if __name__=="__main__":
    main()
