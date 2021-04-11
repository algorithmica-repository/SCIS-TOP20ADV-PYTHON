import sys

def isValid1(out):
    for i in range(1, len(out)):
        for j in range(0,i):
            if(out[i] == out[j] or abs(i-j) == abs(out[i]-out[j])):
                return False
    return True

def auxNqueens1(q, out):
    if(q == len(out)):
        if(isValid1(out)):
            print(out)
        return
    for c in range(len(out)):
        out[q] = c
        auxNqueens1(q+1, out)
        
def nqueens1(n):
    out = [0]*n
    auxNqueens1(0, out)
#------------------------------------
def isValid2(q, c, out):
    for i in range(0, q):
        if(out[i] == c or abs(i-q) == abs(out[i]-c)):
            return False
    return True

def auxNqueens2(q, out):
    if(q == len(out)):
        print(out)
        return
    for c in range(len(out)):
        if(isValid2(q, c, out)):
            out[q] = c
            auxNqueens2(q+1, out)
        
def nqueens2(n):
    out = [0]*n
    auxNqueens2(0, out)
#------------------------------------  
def main():
    n = int(sys.argv[1])
    nqueens2(n)
    
if __name__=="__main__":
    main()
