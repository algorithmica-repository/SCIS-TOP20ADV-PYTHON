import sys


def isPal(s, start, end):
    while(start < end):
        if(s[start] == s[end]):
            start += 1
            end -= 1
        else:
            return False
    return True

#TC:O(n^3)   SC:O(1)
def longPalSubstr1(s):
    n = len(s)
    for i in range(n,0,-1):
        for j in range(0, n-i+1):
            if(isPal(s, j, j+i-1)):
                return s[j:j+i]
    return ""
#-------------------------------------
#TC:O(n^2)   SC:Theta(n^2)
def longPalSubstr2(s):
    n = len(s)
    mem = [ [True]*n for i in range(n)]
    
    maxlen = 0
    pos = 0
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if(s[i] == s[j]):
                mem[i][j] = mem[i+1][j-1]
                if(mem[i][j]):
                    if(j-i+1 > maxlen):
                        maxlen = j-i+1
                        pos = i
            else:
                mem[i][j] = False
    return s[pos:pos+maxlen]
#-------------------------------------
def expandPal(s, left, right):
    l = 0
    while(left >= 0 and right < len(s)):
        if(s[left] == s[right]):
            l += 2
            left -= 1
            right += 1
        else:
            break
    return l

#TC:O(n^2)   SC:O(1)
def longPalSubstr3(s):
    maxlen = 0
    for i in range(len(s)):
       odd = expandPal(s, i-1, i+1) + 1
       even = expandPal(s, i, i+1)
       maxlen = max(maxlen, max(odd, even))
    return maxlen
    
#-------------------------------------
def main():
    print(sys.argv[1])
    print(longPalSubstr1(sys.argv[1]))
    print(longPalSubstr2(sys.argv[1]))
    print(longPalSubstr3(sys.argv[1]))
    
if __name__=="__main__":
    main()
