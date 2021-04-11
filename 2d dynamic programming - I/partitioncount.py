import sys

#TC:Theta(n^3)   SC:Theta(n^2)
def partitionCount31(n):
    mem = [[0]*(n+1) for i in range(n+1)]
    for j in range(1, n+1):
        mem[0][j] = mem[1][j] = mem[j][1] = 1
    for i in range(2, n+1):
        for j in range(2, n+1):
            if(j > i):
                mem[i][j] = mem[i][i]
            else:
                sum = 0
                for k in range(j, 0, -1):
                    sum += mem[i-k][k]
                mem[i][j] = sum
    print(mem)
    return mem[n][n]

#TC:Theta(n^3)   SC:Theta(n^2)
def partitionCount32(n):
    mem = [[0]*(n+1) for i in range(n+1)]
    for j in range(1, n+1):
        mem[0][j] = mem[1][j] = mem[j][1] = 1
    for i in range(2, n+1):
        for j in range(2, n+1):
            if(j > i):
                mem[i][j] = mem[i][i]
            else:
                mem[i][j] = mem[i][j-1] + mem[i-j][j]
    print(mem)
    return mem[n][n]
def main():
    n = int(sys.argv[1])
    print(n)
    print(partitionCount31(n))
    print(partitionCount32(n))
    
if __name__=="__main__":
    main()
