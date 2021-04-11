import sys
import random

def maxMatchings(tea_cups, saucers):
    tea_cups = sorted(tea_cups)
    saucers = sorted(saucers)
    i = 0
    j = 0
    nmatches = 0
    while(i < len(tea_cups) and j < len(saucers)):
        if(tea_cups[i] <= saucers[j]):
            i += 1
            j += 1
            nmatches += 1
        else:
            j += 1
    return nmatches

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    
    tea_cups = [0]*m
    saucers = [0]*n
    
    for i in range(m):
        tea_cups[i] = random.randint(1, 10)
    for i in range(n):
        saucers[i] = random.randint(1, 10) 
    print(tea_cups)
    print(saucers)
    print(maxMatchings(tea_cups, saucers))
    
    
if __name__=="__main__":
    main()
