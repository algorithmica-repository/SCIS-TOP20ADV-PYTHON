import sys

#TODO: Fillup the expression evaluation logic
def getResult(out):
    return 0

def auxEval1(inp, out, target):
    if(len(inp) == 0):
        if(getResult(out) == target):
            print(out)
        return
    auxEval1(inp[1:], out+"+"+inp[0], target)
    auxEval1(inp[1:], out+"-"+inp[0], target)

#TC:Theta(n*2^n-1)   SC:Theta(n)
def eval1(inp, target):
    auxEval1(inp[1:], inp[0], target)
#------------------------------------------------
def digit(c):
    return ord(c) - ord('0')

def auxEval2(inp, out, target, res):
    if(len(inp) == 0):
        if(res == target):
            print(out)
        return
    auxEval2(inp[1:], out+"+"+inp[0], target, res+digit(inp[0]) )
    auxEval2(inp[1:], out+"-"+inp[0], target, res-digit(inp[0]) )

#TC:Theta(2^n-1)   SC:Theta(n)    
def eval2(inp, target):
    auxEval2(inp[1:], inp[0], target, digit(inp[0]) )
#------------------------------------------------  
    
def main():
    target = int(sys.argv[2])
    eval2(sys.argv[1], target)
    
if __name__=="__main__":
    main()
