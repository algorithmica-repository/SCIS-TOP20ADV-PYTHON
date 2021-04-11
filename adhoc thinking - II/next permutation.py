import sys
import random

def swap(inp, i, j):
    tmp = inp[i]
    inp[i] = inp[j]
    inp[j] = tmp

def reverse(inp, i, j):
    while(i < j):
        swap(inp, i, j)
        i += 1
        j -= 1
    
#4 5 3 2 1
#5 4 3 2 1
#TC:Theta(n)   SC:O(1)
def nextPerm(inp):
    n = len(inp)
    i = n - 2
    while(i >= 0):
       if(inp[i] < inp[i+1]):
           break
       i -= 1
       
    if(i < 0):
        return
      
    for j in range(i+1, n):
        if(inp[j] > inp[i]):
            min_ind = j
        else:
            break
    swap(inp, i, min_ind)
    reverse(inp, i+1, n-1)

def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, n)
    print(inp)
    nextPerm(inp)
    print(inp)
    nextPerm(inp)
    print(inp)
    nextPerm(inp)
    print(inp)
    
    
if __name__=="__main__":
    main()
