import sys
import binarytreeutils as utils

#TC:Theta(n^2)   SC:Theta(n)
def maxNonAdjacentSum1(root):
    if(root == None):
        return 0
    if(root.left == None and root.right == None):
        return max(0, root.data)
    incl_sum = root.data
    if(root.left != None):
        if(root.left.left != None):
            incl_sum += maxNonAdjacentSum1(root.left.left)
        if(root.left.right != None):
            incl_sum += maxNonAdjacentSum1(root.left.right)
    if(root.right != None):
        if(root.right.left != None):
            incl_sum += maxNonAdjacentSum1(root.right.left)
        if(root.right.right != None):
            incl_sum += maxNonAdjacentSum1(root.right.right)
            
    excl_sum = 0
    if(root.left != None):
        excl_sum += maxNonAdjacentSum1(root.left)
    if(root.right != None):
        excl_sum += maxNonAdjacentSum1(root.right)
    return max(incl_sum, excl_sum)
#----------------------------------------------------
#TC:Theta(n)   SC:Theta(n)
def maxNonAdjacentSum2(root):
    mem = {}
    auxNonAdjacentSum2(root, mem)
    return mem[root]

def auxNonAdjacentSum2(root, mem):
    if(root == None):
        return 0
    if(root.left == None and root.right == None):
        return max(0, root.data)
    if(mem.get(root) != None):
        return mem[root]
    incl_sum = root.data
    if(root.left != None):
        if(root.left.left != None):
            incl_sum += auxNonAdjacentSum2(root.left.left, mem)
        if(root.left.right != None):
            incl_sum += auxNonAdjacentSum2(root.left.right, mem)
    if(root.right != None):
        if(root.right.left != None):
            incl_sum += auxNonAdjacentSum2(root.right.left, mem)
        if(root.right.right != None):
            incl_sum += auxNonAdjacentSum2(root.right.right, mem)
            
    excl_sum = 0
    if(root.left != None):
        excl_sum += auxNonAdjacentSum2(root.left, mem)
    if(root.right != None):
        excl_sum += auxNonAdjacentSum2(root.right, mem)
    res = max(incl_sum, excl_sum)
    mem[root ] = res
    return res
#------------------------------------------------------------
#TC:Theta(n)   SC:Theta(n)
def maxNonAdjacentSum3(root):
    res = auxNonAdjacentSum3(root)
    return res[0]

def auxNonAdjacentSum3(root):
    if(root == None):
        return (0, 0)
    if(root.left == None and root.right == None):
        return (max(0, root.data), 0)

    left = auxNonAdjacentSum3(root.left)
    right = auxNonAdjacentSum3(root.right)
    
    incl_sum = root.data + left[1] + right[1]
    excl_sum = left[0] + right[0]
    return (max(incl_sum, excl_sum), left[0] + right[0])
#----------------------------------------------------
def main():
    n = int(sys.argv[1])
    root = utils.randomBinaryTree(n)
    #utils.display(root)
    #print(maxNonAdjacentSum1(root))
    print(maxNonAdjacentSum2(root))
    print(maxNonAdjacentSum3(root))
    
if __name__=="__main__":
    main()
