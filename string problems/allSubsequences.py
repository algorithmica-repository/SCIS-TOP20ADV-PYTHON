import sys

def auxSubsequences1(inp, out):
# =============================================================================
#     if(len(inp) == 0):
#         print(out)
#         return
# =============================================================================
    print(out)
    for i in range(len(inp)):
        auxSubsequences1(inp[i+1:],out+inp[i])

#TC:theta(2^n)  SC:theta(n)
def subsequences1(inp):
    auxSubsequences1(inp, "")
#----------------------------------------------  
def auxSubsequences2(inp, out):
    if(len(inp) == 0):
        print(out)
        return
    auxSubsequences2(inp[1:],out+inp[0])
    auxSubsequences2(inp[1:],out)

#TC:theta(2^n+1)  SC:theta(n)
def subsequences2(inp):
    auxSubsequences2(inp, "")
#---------------------------------------------- 
#TC:theta(n*2^n)  SC:O(1)
def subsequences3(inp):
    n = len(inp)
    for i in range(0, 1<<n):
        for j in range(0,n):
            if( (i & (1<<j)) != 0):
                print(inp[j], end="")
        print()
#---------------------------------------------- 
    
def main():
    subsequences3(sys.argv[1])
    
if __name__=="__main__":
    main()
