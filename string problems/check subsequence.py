import sys

#TC:Theta(n)   SC:O(1)
def isSubseq(s1, s2):
    i = 0
    j = 0
    while(i < len(s1)  and j < len(s2)):
        if(s1[i] == s2[j]):
            i += 1
        j += 1
    if(i < len(s1)):
        return False
    return True

def main():
   print(sys.argv[1])
   print(sys.argv[2])
   print(isSubseq(sys.argv[1], sys.argv[2]))
    
if __name__=="__main__":
    main()
