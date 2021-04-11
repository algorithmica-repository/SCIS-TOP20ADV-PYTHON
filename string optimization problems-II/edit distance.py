import sys

def traceOptimalRoute(s1, s2, mem):
    n = len(s1)
    m = len(s2)  
    i = 0
    j = 0
    while(i < n and j < m):
        if(s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            ic = mem[i][j+1]
            dc = mem[i+1][j]
            rc = mem[i+1][j+1]
            if(ic < dc):
                if(ic < rc):
                    print("Insert character ",s2[j])
                    j += 1
                else:
                    print("Repace character ",s1[i], " with ", s2[j])
                    i += 1
                    j += 1
            else:
                if(dc < rc):
                    print("Delete character ",s1[i])
                    i += 1
                else:
                    print("Repace character ",s1[i], " with ", s2[j])
                    i += 1
                    j += 1
    if(i < n):
        print("Delete characters ", s1[i:])
    if(j < m):
        print("Insert characters ", s2[j:])
        
#TC:Theta(mn) SC:theta(mn)
def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    mem = [ [0]*(m+1) for i in range(n+1)]
    
    for j in range(0, m+1):
        mem[n][j] = m-j
    for i in range(0, n+1):
        mem[i][m] = n-i
        
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if(s1[i] == s2[j]):
                mem[i][j] = mem[i+1][j+1]
            else:
                mem[i][j] = min(mem[i][j+1], min(mem[i+1][j], mem[i+1][j+1])) + 1
    print(mem)
    traceOptimalRoute(s1, s2, mem)
    return mem[0][0]

def main():
    print(sys.argv[1])
    print(sys.argv[2])
    print(editDistance(sys.argv[1], sys.argv[2]))
    
if __name__=="__main__":
    main()
