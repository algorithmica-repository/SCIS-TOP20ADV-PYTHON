import sys
import random

def update(tt, inp, i, j):
    if(inp[tt[i]] < inp[tt[j]]):
        tt[(i-1)//2] = tt[i]
    else:
       tt[(i-1)//2] = tt[j] 
    
#2 4 6 2
#0 0 0 0 1 2 3
def secondSmallest(inp):
    n = len(inp)
    tt = [0]*(2*n-1)
    ind = len(tt) - 1
    for i in range(n-1, -1, -1):
        tt[ind] = i
        ind -= 1 
    print(tt)
    
    #build tournament tree
    ind = len(tt)-1
    while(ind > 0):
        if(inp[tt[ind]] < inp[tt[ind-1]]):
            tt[(ind-1)//2] = tt[ind]
        else:
           tt[(ind-1)//2] = tt[ind-1] 
        ind -= 2    
    print(tt)
    print(inp[tt[0]])
    
    #find second smallest
    inp[tt[0]] = sys.maxsize
    ind = tt[0] + n - 1
    while(ind > 0):
        if(ind % 2 == 0):
            update(tt, inp, ind, ind-1)
        else:
            update(tt, inp, ind, ind+1)
        ind = (ind-1)//2
    print(tt)
    return inp[tt[0]]
    

def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, 2*n)
    print(inp)
    print(secondSmallest(inp))
    
if __name__=="__main__":
    main()
