import sys

def traceOptimalRoute(s1, s2, mem):
    i = 0
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(s1[i] == s2[j]): 
            print(s1[i], end='')
            i += 1
            j += 1
        elif(mem[i][j+1] > mem[i+1][j]):
            j += 1
        else:
            i += 1
    print()
            
#TC:Theta(mn)   SC:Theta(mn)
def longComSubseq(s1, s2):
    n = len(s1)
    m = len(s2)
    mem = [[0]*(m+1) for i in range(n+1)]
    
    for i in range(0, n+1):
        mem[i][m] = 0
    for j in range(0, m+1):
        mem[n][j] = 0
        
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if(s1[i] == s2[j]):
                mem[i][j] = 1 + mem[i+1][j+1]
            else:
                mem[i][j] = max(mem[i][j+1], mem[i+1][j])
    print(mem)
    traceOptimalRoute(s1, s2, mem)
    return mem[0][0]

def main():
    print(sys.argv[1])
    print(sys.argv[2])
    print(longComSubseq(sys.argv[1], sys.argv[2]))
    
if __name__=="__main__":
    main()
