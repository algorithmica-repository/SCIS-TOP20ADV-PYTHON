import sys
import random

class UnionbySizeDisjointSet():
    def __init__(self, n):
        self.parent = [0]*n
        self.rank = [0]*n
        self.sz = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
    
    #TC:O(log n)
    def find(self, x):
        while(self.parent[x] != x):
            x = self.parent[x]
        return x
    
    #TC:O(log n)
    def union(self, x,y):
        idx = self.find(x)
        idy = self.find(y)
        if(idx == idy):
            return
        self.sz -= 1
        if(self.rank[idx] > self.rank[idy]):
            self.parent[idy] = idx
            self.rank[idx] += self.rank[idy]
        else:
            self.parent[idx] = idy
            self.rank[idy] += self.rank[idx]
            
    #O(1)
    def size(self):
        return self.sz
    
    def display(self):
        print(self.parent)
        print(self.rank)

def main():
    n = int(sys.argv[1])
    s1 = UnionbySizeDisjointSet(n)
    s1.display()
    for i in range(n//2):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        print(x, y)
        s1.union(x, y)
        s1.display()
    print(s1.size())
    print(s1.find(0))
    print(s1.find(n-1))
    
if __name__=="__main__":
    main()