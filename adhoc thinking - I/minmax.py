import sys
import random

#~2n comparisons
def minMax1(inp):
    if(inp[0] < inp[1]):
        min = inp[0]
        max = inp[1]
    else:
        min = inp[1]
        max = inp[0]        
    
    for i in range(2, len(inp)):
        if(inp[i] < min):
            min = inp[i]
        elif(inp[i] > max):
            max = inp[i]
    print(min)
    print(max)

#~1.5n comparisons
def minMax2(inp):
    if(inp[0] < inp[1]):
        min = inp[0]
        max = inp[1]
    else:
        min = inp[1]
        max = inp[0]        
    
    for i in range(2, len(inp)-1, 2):
        if(inp[i] < inp[i+1]):
            pmin = inp[i]
            pmax = inp[i+1]
        else:
            pmin = inp[i+1]
            pmax = inp[i]  
            
        if(pmin < min):
            min = pmin
        if(pmax > max):
            max = pmax
    if(i < len(inp)):
        if(inp[i] < min):
            min = inp[i]
        elif(inp[i] > max):
            max = inp[i]        
    print(min)
    print(max)
    
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, 2*n)
    print(inp)
    minMax1(inp)
    minMax2(inp)
    
if __name__=="__main__":
    main()
