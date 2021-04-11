import sys
from radixtrie import RadixTrie

def prefixLen(s1, s2, i, j):
    clen = 0
    while i < len(s1) and j < len(s2):
        if(s1[i] == s2[j]):
            i += 1
            j += 1
            clen += 1
        else:
            break
    return clen

#TC:O(n^3)  SC:O(1)
def longCommSubst2(s1, s2):
    maxlen = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            clen = prefixLen(s1, s2, i, j)
            maxlen = max(clen, maxlen)
    return maxlen
#-----------------------------------------------
    
#TC:O(n^2 log n)  SC:Theta(n^2)
def longCommSubst3(s1, s2):
    suffix_array = []
    for i in range(len(s1)):
        suffix_array.append(s1[i:] + "#")
    for i in range(len(s2)):
        suffix_array.append(s2[i:] + "$")
    #print(suffix_array)
    suffix_array = sorted(suffix_array)
    #print(suffix_array)
    
    maxlen = 0
    for i in range(1, len(suffix_array)):
        if( (suffix_array[i-1][-1] == '#' and suffix_array[i][-1] == '$') or 
            (suffix_array[i-1][-1] == '$' and suffix_array[i][-1] == '#') ):
            clen = prefixLen(suffix_array[i-1], suffix_array[i], 0, 0)
            maxlen = max(clen, maxlen)
    return maxlen
#-----------------------------------------------
    
#TC:O(n^2)  SC:Theta(n^2)
def longCommSubst4(s1, s2):
    maxlen = 0
    trie = RadixTrie()
    for i in range(len(s1)):
        trie.add(s1[i:])
    for i in range(len(s2)):
        res = trie.lcp(s2[i:])
        maxlen = max(len(res), maxlen)                
    return maxlen
#-----------------------------------------------
    
#TC:O(n^2)  SC:Theta(n^2)
def longCommSubst5(s1, s2):
    mem = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
    for j in range(len(s2)+1):
        mem[len(s1)][j] = 0
    for i in range(len(s1)+1):
        mem[i][len(s2)] = 0        
    
    maxlen = 0
    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)):
            if(s1[i] == s2[j]):
                mem[i][j] = 1 + mem[i+1][j+1]
                maxlen = max(maxlen, mem[i][j])
            else:
                mem[i][j] = 0
    print(mem)
    return maxlen
#-----------------------------------------------
    
def main():
    print(sys.argv[1])
    print(sys.argv[2])
    print(longCommSubst5(sys.argv[1], sys.argv[2]))
    
if __name__=="__main__":
    main()
