import sys

def isValid1(out):
    for i in range(len(out)):
        if(i == 0 or i % 2 == 0):
            if(out[i] % 2 != 0):
                return False
        else:
            if(out[i] % 3 != 0):
                return False
    return True

def auxArrangements1(i, out):
    if(i == len(out)):
        if(isValid1(out)):
            print(out)
        return
    for d in range(1, 10):
        out[i] = d
        auxArrangements1(i+1, out)

#TC:Theta(9^n)   SC:Theta(n)       
def arrangements1(n):
    out = [0]*n
    auxArrangements1(0, out)
#---------------------------------------
def isValid2(i, d):
    if(i == 0 or i % 2 == 0):
        if(d % 2 != 0):
            return False
    else:
        if(d % 3 != 0):
            return False
    return True

def auxArrangements2(i, out):
    if(i == len(out)):
        print(out)
        return
    for d in range(1, 10):
        if(isValid2(i, d)):
            out[i] = d
            auxArrangements2(i+1, out)

#TC:Theta(9^n)   SC:Theta(n)       
def arrangements2(n):
    out = [0]*n
    auxArrangements2(0, out)
#---------------------------------------
    
def main():
    n = int(sys.argv[1])
    arrangements2(n)
    
if __name__=="__main__":
    main()
