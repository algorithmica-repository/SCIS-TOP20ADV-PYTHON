import sys
import binarytreeutils as utils

class MyInteger():
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def set(self, val):
        self.val = val
        
def auxMaxSum1(root, csum, gmax):
    if(root == None):
        return
    if(root.left == None and root.right == None):
        gmax.set(max(gmax.get(), csum +root.data))
        return
    auxMaxSum1(root.left, csum + root.data, gmax)
    auxMaxSum1(root.right, csum + root.data, gmax)

#TC:Theta(n)   SC:Theta(n)
def maxSum1(root):
    gmax = MyInteger(0)
    auxMaxSum1(root, 0, gmax)
    return gmax.get()

#TC:Theta(n)   SC:Theta(n)
def maxSum2(root):
    if(root == None):
        return 0
    if(root.left == None and root.right == None):
        return root.data
    left = maxSum2(root.left)
    right = maxSum2(root.right)
    return max(left, right) + root.data

def main():
    n = int(sys.argv[1])
    root = utils.randomBinaryTree(n)
    utils.display(root)
    print(maxSum1(root))
    print(maxSum2(root))
    
if __name__=="__main__":
    main()
