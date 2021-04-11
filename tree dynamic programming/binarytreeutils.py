import random
import sys

class TreeNode():
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x


def add(root, x):
    if(root == None):
        return TreeNode(x)
    
    root_copy = root
    while(True):
        outcome = random.randint(0,2)
        if(outcome == 0):
            if(root.left == None):
                root.left = TreeNode(x)
                break
            root = root.left
        else:
            if(root.right == None):
                root.right = TreeNode(x)
                break
            root = root.right
    return root_copy

def randomBinaryTree(n):
    root = None
    for i in range(n):
        root = add(root, i+1)
    return root

def oneSidedBinaryTree(n):
    root = TreeNode(random.randint(1,3*n))
    current = root
    for i in range(n-1):
        current.right = TreeNode(random.randint(1,2*n))
        current = current.right
    return root

def auxDisplay(root, nspaces, annotation):
    if(root == None):
        return
    for i in range(nspaces):
        print(" ", end=" ")
    print(root.data, "(", annotation , ")")
    auxDisplay(root.left, nspaces + 4, "L")
    auxDisplay(root.right, nspaces + 4, "R")
    
def display(root):
    auxDisplay(root, 0, "root")

def main():
    n = int(sys.argv[1])
    root = randomBinaryTree(n)
    display(root)

if __name__ == "__main__":
    main()

 
        