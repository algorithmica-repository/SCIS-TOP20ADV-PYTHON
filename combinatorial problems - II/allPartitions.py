import sys

def auxPartitions(inp, out):
    if(len(inp) == 0):
        print(out)
        return
    sep = ""
    for i in range(len(inp)):
        if(len(out) != 0):
            sep = "+"
        auxPartitions(inp[i+1:], out + sep + inp[:i+1])

#TC:Theta(2^n)   SC:Theta(n)   
def partitions(inp):
    auxPartitions(inp, "")

def main():
    partitions(sys.argv[1])
    
if __name__=="__main__":
    main()
