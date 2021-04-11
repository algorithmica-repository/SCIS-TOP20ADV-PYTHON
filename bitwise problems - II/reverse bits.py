import sys
import bitwiseutils as utils

def reverse(n):
    utils.showBits(n)
    n = ((n & 0x55555555) << 1) | ((n>>1)&0x55555555)
    utils.showBits(n)
    n = ((n & 0x33333333) << 2) | ((n>>2)&0x33333333)
    utils.showBits(n)
    n = ((n & 0x0F0F0F0F) << 4) | ((n>>4)&0x0F0F0F0F)
    utils.showBits(n)
    n = ((n & 0x00FF00FF) << 8) | ((n>>8)&0x00FF00FF)
    utils.showBits(n)
    n = ((n & 0x0000FFFF) << 16) | ((n>>16)&0x0000FFFF)
    utils.showBits(n)
    return n

def main():
    n = int(sys.argv[1])
    reverse(n)
    
if __name__=="__main__":
    main()
