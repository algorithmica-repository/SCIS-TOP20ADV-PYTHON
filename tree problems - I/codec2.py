import sys
import binarytreeutils as utils
from queue import Queue
  
class Codec2():     
    #TC:Theta(n)   SC:Theta(n)
    def ser(self, root):
        res = ""
        q = Queue()
        q.put(root)
        
        while(not q.empty()):
            root = q.get()
            if(root == None):
                res += "#,"
            else:
                res += str(root.data) + ","
                q.put(root.left)
                q.put(root.right)
        
        return res

        
    #TC:Theta(n)   SC:Theta(n)
    def deser(self, s):
        data = s.split(",")
        q = Queue()
        
        i = 0
        root = utils.TreeNode(data[i])
        q.put(root)
        
        while(not q.empty()):
            i += 1
            left_data = data[i]
            i += 1
            right_data = data[i]
            current = q.get()
            
            if(left_data == "#"):
               current.left = None
            else:
               current.left = utils.TreeNode(left_data)
               q.put(current.left)
    
            if(right_data == "#"):
               current.right = None
            else:
               current.right = utils.TreeNode(right_data)
               q.put(current.right)
        return root
        
def main():
    n = int(sys.argv[1])
    root = utils.randomBinaryTree(n)
    utils.display(root)
    c = Codec2()
    data = c.ser(root)
    print(data)
    root = c.deser(data)
    utils.display(root)
    
if __name__=="__main__":
    main()
