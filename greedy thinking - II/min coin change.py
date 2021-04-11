import sys

#TC:Theta(n log n)  SC:O(1)
def minCoins11(n, b, s):
    ncoins = 0
    for i in range(n-1, -1, -1):
        if(s <= 0):
            break
        denom = pow(b, i)
        if(denom <= s):
            ncoins += (s//denom)
            s = s % denom
    return ncoins

#TC:Theta(n)  SC:O(1)
def minCoins12(n, b, s):
    ncoins = 0
    denom = pow(b, n-1)
    while(s > 0):
        if(denom <= s):
            ncoins += (s//denom)
            s = s % denom
        denom //= b
    return ncoins

def main():
    n = int(sys.argv[1])
    b = int(sys.argv[2])
    s = int(sys.argv[3])
    print(n, b, s)
    print(minCoins11(n, b, s))
    print(minCoins12(n, b, s))
    
if __name__=="__main__":
    main()
