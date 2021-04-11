import sys
import random

#TC:Theta(n log n) SC:O(1)
def minWaitingTime(inp):
    inp = sorted(inp)
    job_wt = 0
    total_wt = 0
    for i in range(1, len(inp)):
        job_wt += inp[i-1]
        total_wt += job_wt
    return total_wt
        
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, n)
    print(inp)
    print(minWaitingTime(inp))
    
if __name__=="__main__":
    main()
