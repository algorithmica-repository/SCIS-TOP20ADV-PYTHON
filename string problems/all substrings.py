import sys

#TC:Theta(n^2)  SC:O(1)
def substr1(s):
    for i in range(1, len(s)+1):
        for j in range(0, len(s)-i+1):
            print(s[j:j+i])

#TC:Theta(n^2)  SC:O(1)
def substr2(s):
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])
def main():
    print(sys.argv[1])
    substr1(sys.argv[1])
    substr2(sys.argv[1])
    
if __name__=="__main__":
    main()
