import sys
from queue import PriorityQueue
import random

#TC:Theta(n log n)  SC:Theta(n)
def minCostMerge(inp):
    pq = PriorityQueue()
    for x in inp:
        pq.put(x)
    #print(pq.queue)
    tot = 0
    while(pq.qsize() > 1):
        smallest1 = pq.get()
        smallest2 = pq.get()
        pq.put(smallest1+ smallest2)
        tot += (smallest1+smallest2)
    return tot
    
def main():
    n = int(sys.argv[1])
    inp = [0]*n
    for i in range(n):
        inp[i] = random.randint(1, 10)
    print(inp)
    print(minCostMerge(inp))
    
if __name__=="__main__":
    main()
