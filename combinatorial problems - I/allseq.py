import sys

def auxAllSeq(n, inp, out):
    if(n == 0):
        print(out)
        return
    for i in range(len(inp)):
        auxAllSeq(n-1, inp, out+inp[i])

#TC:theta(n^n)   SC:theta(n)      
def allSeq(inp):
    auxAllSeq(len(inp), inp, "")
    
def main():
    allSeq(sys.argv[1])
    
if __name__=="__main__":
    main()
