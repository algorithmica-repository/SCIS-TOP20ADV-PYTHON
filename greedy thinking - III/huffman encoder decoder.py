import sys
import random
from queue import PriorityQueue

class TreeNode():
    def __init__(self, character, freq, left, right):
        self.character = character
        self.freq = freq
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.freq < other.freq
    
class EncoderDecoder():
    def __init__(self):
        self.root = None
        
    def auxDisplay(self, root, nspaces, annotation):
        if(root == None):
            return
        for i in range(nspaces):
            print(" ", end=" ")
        print(root.character, "(", root.freq, annotation , ")")
        self.auxDisplay(root.left, nspaces + 4, "L")
        self.auxDisplay(root.right, nspaces + 4, "R")
    
    def display(self, root):
        self.auxDisplay(self.root, 0, "root")
        
    def buildTree(self, inp):
        #get the frquencies of characters
        freq = {}
        for x in inp:
            if(freq.get(x) == None):
                freq[x] = 1
            else:
                freq[x] += 1
        print(freq)
        
        #build huffman tree
        pq = PriorityQueue()
        for k,v in freq.items():
            pq.put(TreeNode(k, v, None, None))
        
        while(pq.qsize() > 1):
            smallest1 = pq.get()
            smallest2 = pq.get()
            pq.put(TreeNode('#', smallest1.freq+smallest2.freq, smallest1, smallest2))
        self.root = pq.get()
        self.display(self.root)
    
    def auxEncode(self, root, code, enc):
        if(root == None):
            return
        if(root.left == None and root.right == None):
            enc[root.character] = code
        self.auxEncode(root.left, code+"0", enc)
        self.auxEncode(root.right, code+"1", enc)
    def encode(self, inp):
        #get the encodings
        enc = {}
        self.auxEncode(self.root, "", enc)
        print(enc)
        
        #get the encoded string for input
        res = ""
        for x in inp:
            res += enc[x]
        return res
    
    def isLeaf(self, root):
        return root.left == None and root.right == None
    
    def decode(self, inp):
        res = ""
        i = 0
        while(i < len(inp)):
            current = self.root
            while(not self.isLeaf(current)):
                if(inp[i] == '0'):
                    current = current.left
                else:
                    current = current.right
                i += 1
            res += current.character
        return res
    
def main():
    n = int(sys.argv[1])
    inp = ""
    for i in range(n):
        inp += chr(ord('a') + random.randint(0, 25))
    print(inp)
    
    enc_dec = EncoderDecoder()
    enc_dec.buildTree(inp)
    enc = enc_dec.encode(inp)
    print(enc)
    print(enc_dec.decode(enc))
    
if __name__=="__main__":
    main()
