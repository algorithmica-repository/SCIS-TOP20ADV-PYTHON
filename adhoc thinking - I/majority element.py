import sys
import random

#TC:theta(n)  SC:O(1)
def majority(inp):
    maj = sys.maxsize
    count = 1
    for i in range(len(inp)):
        if(inp[i] == maj):
            count += 1
        else:
            count -= 1
            if(count == 0):
                maj = inp[i]
                count = 1
    return maj

def main():
    n = int(sys.argv[1])
    inp = [0]*n
    maj = random.randint(1, n)
    for i in range(n//2+1):
        inp[i] = maj
    for i in range(n//2+1, n):
        inp[i] = random.randint(1, n)
    print(inp)
    print(majority(inp))
    
if __name__=="__main__":
    main()
