import sys

def showBits(n):
    #size = n.bit_length()
    size = 32
    if(size == 0):
        print(0)
        return
    mask = 1 << (size-1)
    for i in range(size):
        if((n & mask) != 0):
            print(1, end="")
        else:
            print(0, end="")
        mask = mask >> 1
    print()
    
def main():
    n = int(sys.argv[1])
    showBits(n)
    showBits(-n)
    
if __name__=="__main__":
    main()
