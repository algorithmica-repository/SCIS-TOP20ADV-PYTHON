import sys

class Superstack1():
    
    def __init__(self):
        self.data_stack = []
        self.max_stack = []
    
    #TC:O(1)
    def push(self, x):
        self.data_stack.append(x)
        if(not self.max_stack or x > self.max_stack[-1]):
            self.max_stack.append(x)
    
    #TC:O(1)
    def pop(self):
        if(not self.data_stack):
            return sys.maxsize
        res = self.data_stack.pop()
        if(self.max_stack[-1] == res):
            self.max_stack.pop()
        return res

    #TC:O(1)    
    def max(self):
        if(not self.data_stack):
            return sys.maxsize
        return self.max_stack[-1]  

    def display(self):
        print(self.data_stack)
        
def main():
    #n = int(sys.argv[1])
    ss = Superstack1()
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
