import sys
import bitwiseutils as utils

def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    utils.showBits(n) 
    utils.showBits(m) 
    utils.showBits(n & m) 
    utils.showBits(n | m) 
    utils.showBits(n ^ m) 
    utils.showBits(n << 2) 
    utils.showBits(n >> 2) 
    utils.showBits(~n) 
    
if __name__=="__main__":
    main()
