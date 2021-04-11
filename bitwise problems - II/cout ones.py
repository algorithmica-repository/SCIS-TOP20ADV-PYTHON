import sys
import bitwiseutils as utils

def countOnes1(n):
    size = 32
    mask = 1 << (size-1)
    n_ones = 0
    for i in range(size):
        if((n & mask) != 0):
            n_ones += 1
        mask = mask >> 1
    return n_ones

def countOnes2(n):
    n_ones = 0
    while(n > 0):
        n = n & (n-1)
        n_ones += 1
    return n_ones

def countOnes3(n):
    ones = [0, 1, 1, 2]
    n_ones = 0
    while(n > 0):
        n_ones += ones[n & 3]
        n = n >> 2
    return n_ones

def main():
    n = int(sys.argv[1])
    utils.showBits(n)
    print(countOnes1(n))
    print(countOnes2(n))
    print(countOnes3(n))
    
if __name__=="__main__":
    main()
