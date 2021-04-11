import sys
import binarytreeutils as utils

#TC:Theta(n)   SC:Theta(n)
def preOrderR(root):
    if(root == None):
        return
    print(root.data)
    preOrderR(root.left)
    preOrderR(root.right)

#TC:Theta(n)   SC:Theta(n)
def preOrderNR(root):
    s = []
    while(True):
        while(root != None):
            s.append(root)
            print(root.data)
            root = root.left
        if(len(s) == 0):
            break
        root = s.pop().right    
    
def main():
    n = int(sys.argv[1])
    root = utils.oneSidedBinaryTree(n)
    #utils.display(root)
    #preOrderR(root)
    preOrderNR(root)
    
if __name__=="__main__":
    main()
