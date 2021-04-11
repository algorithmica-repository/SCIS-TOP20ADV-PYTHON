import sys

class Superstack2():
    
    def __init__(self):
        self.data_stack = []
        self.mx = sys.maxsize
    
    #TC:O(1)
    def push(self, x):
        if(x > self.mx):
            self.data_stack.append(2*x-self.mx)
            self.mx = x
        else:
            if(not self.data_stack):
                self.mx = x
            self.data_stack.append(x)
    
    #TC:O(1)
    def pop(self):
        if(not self.data_stack):
            return sys.maxsize
        res = self.data_stack.pop()
        if(res > self.mx):
            tmp = self.mx
            self.mx = 2*self.mx-res
        else:
            tmp = res
        return tmp

    #TC:O(1)    
    def max(self):
        if(not self.data_stack):
            return sys.maxsize
        return self.mx  

    def display(self):
        print(self.data_stack)
        
def main():
    #n = int(sys.argv[1])
    ss = Superstack2()
    for i in range(1, 11):
        ss.push(i)
        ss.display()
    print(ss.max())
    for i in range(1, 6):
        print(ss.pop())
        ss.display()   
    print(ss.max())
    
if __name__=="__main__":
    main()
