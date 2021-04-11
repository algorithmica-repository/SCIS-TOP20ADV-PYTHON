import sys
import binarytreeutils as utils

#TC:Theta(n)   SC:Theta(n)
def inOrderR(root):
    if(root == None):
        return
    inOrderR(root.left)
    print(root.data)
    inOrderR(root.right)

#TC:Theta(n)   SC:Theta(n)
def inOrderNR(root):
    s = []
    while(True):
        while(root != None):
            s.append(root)
            root = root.left
        if(len(s) == 0):
            break
        root = s.pop()
        print(root.data)
        root = root.right    
    
def main():
    n = int(sys.argv[1])
    root = utils.oneSidedBinaryTree(n)
    #utils.display(root)
    inOrderR(root)
    inOrderNR(root)
    
if __name__=="__main__":
    main()
