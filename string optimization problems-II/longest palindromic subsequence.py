import sys

def traceOptimalRoute(s, mem):
    i = 0
    j = len(s)-1
    res = ""
    while(i < j):
       if(s[i] == s[j]):
           res += s[i]
           i += 1
           j -= 1
       elif(mem[i+1][j] > mem[i][j-1]):
           i += 1
       else:
           j -= 1
    if(i == j):
        print(res + s[i] + res[::-1])
    else:
        print(res+res[::-1])
        

#TC:Theta(n^2)  SC:Theta(n^2)
def longPalSubseq(s):
    n = len(s)
    mem = [[0]*n for i in range(n)]
    for i in range(n):
        mem[i][i] = 1
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if(s[i] == s[j]):
                mem[i][j] = 2 + mem[i+1][j-1]
            else:
                mem[i][j] = max(mem[i+1][j], mem[i][j-1])
    print(mem)
    traceOptimalRoute(s, mem)
    return mem[0][n-1]

def main():
   print(sys.argv[1])
   print(longPalSubseq(sys.argv[1]))
    
if __name__=="__main__":
    main()
