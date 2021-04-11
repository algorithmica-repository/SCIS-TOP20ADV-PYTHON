import sys

class RadixNode():
    def __init__(self):
        self.isword = False
        self.children = {}
        self.words = []
        
class RadixTrie():
    def __init__(self):
        self.root = RadixNode()
    
    def add(self, word):
        current = self.root
        for c in word:
            ind = c
            if(current.children.get(ind) == None):
               current.children[ind] = RadixNode() 
            current.words.append(word)
            current = current.children[ind]
        current.isword = True
        current.words.append(word)
    
    def findLastNode(self, word):
        current = self.root
        for c in word:
            ind = c
            if(current.children.get(ind) == None):
               return None
            current = current.children[ind]  
        return current
            
    def contains(self, word):
        res = self.findLastNode(word)
        if(res == None):
            return False
        return res.isword
            
    def startsWith(self, prefix):
        res = self.findLastNode(prefix)
        if(res == None):
            return None
        return res.words
    
    def lcp(self, word):
        current = self.root
        i = 0
        for c in word:
            ind = c
            if(current.children.get(ind) == None):
               break
            current = current.children[ind] 
            i += 1
        return word[:i]
    