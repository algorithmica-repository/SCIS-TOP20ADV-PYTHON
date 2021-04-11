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
    
class Codec1():
    def auxSer(self, root, res):
        if(root == None):
            res.append("#," )
            return
        res.append(str(root.data) + ",")
        self.auxSer(root.left, res)
        self.auxSer(root.right, res)
     
    #TC:Theta(n)   SC:Theta(n)
    def ser(self, root):
        res = MyString()
        self.auxSer(root, res)
        return res.get()
    
    def auxDeser(self, data):
        tmp = data.pop(0)
        if(tmp == "#"):
            return None
        root = utils.TreeNode(tmp)
        root.left = self.auxDeser(data)
        root.right = self.auxDeser(data)
        return root
        
    #TC:Theta(n)   SC:Theta(n)
    def deser(self, s):
        data = s.split(",")
        return self.auxDeser(data)
        
def main():
    n = int(sys.argv[1])
    root = utils.randomBinaryTree(n)
    utils.display(root)
    c = Codec1()
    data = c.ser(root)
    print(data)
    root = c.deser(data)
    utils.display(root)
    
if __name__=="__main__":
    main()
