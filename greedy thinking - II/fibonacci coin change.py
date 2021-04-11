import sys

#TC:Theta(log S)  SC:O(1)
def minCoins(s):
    f1 = 0
    f2 = 1
    while(f2 <= s):
        print(f2, end=" ")
        tmp = f1 + f2
        f1 = f2
        f2 = tmp
    print()
    
    ncoins = 0
    while(s > 0):
        if(f1 <= s):
            ncoins += (s // f1)
            s %= f1
        tmp = f2 - f1
        f2 = f1
        f1 = tmp
    return ncoins

def main():
    s = int(sys.argv[1])
    print(s)
    print(minCoins(s))
    
if __name__=="__main__":
    main()
