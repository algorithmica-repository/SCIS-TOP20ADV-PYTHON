import sys
import bitwiseutils as utils

def lowest11(n):
    return n & ~7

def lowest12(n):
    return n & -8

def main():
    n = int(sys.argv[1])
    utils.showBits(n)
    print(lowest11(n))
    print(lowest12(n))
    
if __name__=="__main__":
    main()
