import sys

def auxCombinations1(inp, out):
# =============================================================================
#     if(len(inp) == 0):
#         print(out)
#         return
# =============================================================================
    print(out)
    for i in range(len(inp)):
        auxCombinations1(inp[i+1:],out+inp[i])

#TC:theta(2^n)  SC:theta(n)
def combinations1(inp):
    auxCombinations1(inp, "")
#----------------------------------------------  
def auxCombinations2(inp, out):
    if(len(inp) == 0):
        print(out)
        return
    auxCombinations2(inp[1:],out+inp[0])
    auxCombinations2(inp[1:],out)

#TC:theta(2^n+1)  SC:theta(n)
def combinations2(inp):
    auxCombinations2(inp, "")
#---------------------------------------------- 
#TC:theta(n*2^n)  SC:O(1)
def combinations3(inp):
    n = len(inp)
    for i in range(0, 1<<n):
        for j in range(0,n):
            if( (i & (1<<j)) != 0):
                print(inp[j], end="")
        print()
#---------------------------------------------- 
    
def main():
    combinations3(sys.argv[1])
    
if __name__=="__main__":
    main()
