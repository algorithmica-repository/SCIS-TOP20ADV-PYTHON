import sys

def powerOfTwo1(n):
    size = 32
    mask = 1 << (size-1)
    n_ones = 0
    for i in range(size):
        if((n & mask) != 0):
            n_ones += 1
        mask = mask >> 1
    if(n_ones == 1):
        return True
    return False

def powerOfTwo2(n):
    if(n == 0):
        return False
    return (n & (n-1)) == 0

def main():
    n = int(sys.argv[1])
    print(powerOfTwo1(n))
    print(powerOfTwo2(n))
    
if __name__=="__main__":
    main()
