import sys

class TSTNode():
    def __init__(self, data=''):
        self.isword = False
        self.left = None
        self.middle = None
        self.right = None
        self.data = data
        self.words = []
        
class TSTTrie():
    def __init__(self):
        self.root = TSTNode()
    
    def auxAdd(self, i, word, current):
        if(current == None):
            current = TSTNode(word[i])            
        if(word[i] == current.data):
            if(i < len(word)-1):
                current.middle = self.auxAdd(i+1, word, current.middle)
            if(i == len(word)-1):
                current.isword = True
            current.words.append(word)
        elif(word[i] < current.data):
            current.left = self.auxAdd(i, word, current.left)
        else:
            current.right = self.auxAdd(i, word, current.right)
        return current
        
    def add(self, word):
        self.root.words.append(word)
        res = self.auxAdd(0, word, self.root.middle)
        if(self.root.middle == None):
            self.root.middle = res
    
    def findLastNode(self, word):
        current = self.root.middle
        i = 0
        while(i < len(word)):
           if(current == None): 
                return None
           if(word[i] == current.data):
               if(i < len(word)-1):
                   current = current.middle
               i += 1
           elif(word[i] < current.data):
               current = current.left
           else:
               current = current.right
        return current
            
    def contains(self, word):
        res = self.findLastNode(word)
        if(res == None):
            return False
        return res.isword
            
    def startsWith(self, prefix):
        if(len(prefix) == 0):
            return self.root.words
        res = self.findLastNode(prefix)
        if(res == None):
            return None
        return res.words
    
    def lcp(self, word):
        current = self.root.middle
        i = 0
        while(i < len(word)):
           if(current == None): 
                break
           if(word[i] == current.data):
               current = current.middle
               i += 1
           elif(word[i] < current.data):
               current = current.left
           else:
               current = current.right
        return word[:i]
        
    def auxDisplay(self, root, nspaces, annotation):
        if(root == None):
            return
        for i in range(nspaces):
            print(" ", end=" ")
        print(root.data, "(", annotation , ")" , root.isword, root.words)
        self.auxDisplay(root.left, nspaces + 4, "L")
        self.auxDisplay(root.middle, nspaces + 4, "M")
        self.auxDisplay(root.right, nspaces + 4, "R")
        
    def display(self):
        self.auxDisplay(self.root.middle, 0, "root")        
    
def main():
    words = ["abd", "abc", "ab", "def", "abcd", "xyz", "cat"]
    trie = TSTTrie()
    for word in words:
        trie.add(word)
    
    trie.display()
    
    print(trie.startsWith(""))
    print(trie.startsWith("ab"))
    print(trie.startsWith("ad"))
    print(trie.startsWith("x"))
    
    print(trie.contains("abxy"))
    print(trie.contains("xyz"))
    print(trie.contains("ab"))
    
    print(trie.lcp("abxy"))
    print(trie.lcp("xyz"))
    print(trie.lcp("ab"))
    print(trie.lcp("xyzp"))
    
if __name__=="__main__":
    main()
