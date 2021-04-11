import sys
import binarytreeutils as utils

class MyString():
    def __init__(self):
        self.data = ""
    def append(self, val):
        self.data += val
    def get(self):
        return self.data
    def __repr__(self):
        return self.data
    
class Codec3():
    def auxIn(self, root, res):
        if(root == None):
            return
        self.auxIn(root.left, res)
        res.append(str(root.data) + ",")
        self.auxIn(root.right, res)
        
    def auxPre(self, root, res):
        if(root == None):
            return
        res.append(str(root.data) + ",")
        self.auxPre(root.left, res)
        self.auxPre(root.right, res)
     
    #TC:Theta(n)   SC:Theta(n)
    def ser(self, root):
        res = MyString()
        self.auxIn(root, res)
        res.append("#")
        self.auxPre(root, res)
        return res.get()
    
    def findPosition(self, in_order, tmp):
        for i in range(len(in_order)):
            if(tmp == in_order[i]):
                return i
        return -1
    
    def auxDeser(self, pre_order, in_order, l, r):
        if(l > r):
            return None
        tmp = pre_order.pop(0)
        root = utils.TreeNode(tmp)
        p = self.findPosition(in_order, tmp)
        root.left = self.auxDeser(pre_order, in_order, l, p-1)
        root.right = self.auxDeser(pre_order, in_order, p+1, r)
        return root
        
    #TC:Theta(n)   SC:Theta(n)
    def deser(self, s):
        orders = s.split("#")
        in_order = orders[0].split(",")[:-1]
        pre_order = orders[1].split(",")[:-1]
        #print(in_order)
        #print(pre_order)
        return self.auxDeser(pre_order, in_order, 0, len(in_order)-1)
        
def main():
    n = int(sys.argv[1])
    root = utils.randomBinaryTree(n)
    utils.display(root)
    c = Codec3()
    data = c.ser(root)
    print(data)
    root = c.deser(data)
    utils.display(root)
    
if __name__=="__main__":
    main()
