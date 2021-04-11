import sys
import bitwiseutils as utils

def highest11(n):
    return (n+7) & ~7

def highest12(n):
    return (n+7) & -8

def main():
    n = int(sys.argv[1])
    utils.showBits(n)
    print(highest11(n))
    print(highest12(n))
    
if __name__=="__main__":
    main()
