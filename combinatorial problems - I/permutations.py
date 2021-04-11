import sys

def isValid1(out):
    for i in range(1, len(out)):
        for j in range(0, i):
            if(out[i] == out[j]):
                return False
    return True

def auxPermutations1(n, inp, out):
    if(n == 0):
        if(isValid1(out)):
            print(out)
        return
    for i in range(len(inp)):
        auxPermutations1(n-1, inp, out+inp[i])

#TC:theta(n^n+1)   SC:theta(n)      
def permutations1(inp):
    auxPermutations1(len(inp), inp, "")
#------------------------------------------------- 
def isValid2(c, out):
    for i in range(0, len(out)):
        if(out[i] == c):
                return False
    return True

def auxPermutations2(n, inp, out):
    if(n == 0):
        print(out)
        return
    for i in range(len(inp)):
        if(isValid2(inp[i], out)):
            auxPermutations2(n-1, inp, out+inp[i])

#TC:theta(n^n)   SC:theta(n)      
def permutations2(inp):
    auxPermutations2(len(inp), inp, "")
#------------------------------------------------- 
def auxPermutations3(inp, out):
    if(len(inp) == 0):
        print(out)
        return
    for i in range(len(inp)):
         auxPermutations3(inp[:i]+inp[i+1:], out+inp[i])

#TC:theta(n^n)   SC:theta(n)      
def permutations3(inp):
    auxPermutations3(inp, "")
#------------------------------------------------- 
def main():
    permutations3(sys.argv[1])
    
if __name__=="__main__":
    main()