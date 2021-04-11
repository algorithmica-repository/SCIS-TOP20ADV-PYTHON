import sys
import random

#TC:Theta(n)  SC:Theta(n)
def minCandies(inp):
    candies = [0]*(len(inp))
    
    #left to right scan
    candies[0] = 1
    for i in range(1, len(inp)):
        if(inp[i] > inp[i-1]):
            candies[i] = candies[i-1] + 1
        else:
            candies[i] = 1
    print(candies)
    
    total = candies[len(inp)-1]
    #right to left scan
    for i in range(len(inp)-2, -1, -1):
        if(inp[i] > inp[i+1] and candies[i] <= candies[i+1]):
            candies[i] = candies[i+1] + 1
        total += candies[i]
    print(candies)
    return total
    
    
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, 10)
    print(inp)  
    print(minCandies(inp))
    
if __name__=="__main__":
    main()

