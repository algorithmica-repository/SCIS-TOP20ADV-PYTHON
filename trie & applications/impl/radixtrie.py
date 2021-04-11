import sys

class RadixNode():
    def __init__(self):
        self.isword = False
        self.children = [None]*26
        self.words = []
        
class RadixTrie():
    def __init__(self):
        self.root = RadixNode()
    
    def add(self, word):
        current = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if(current.children[ind] == None):
               current.children[ind] = RadixNode() 
            current.words.append(word)
            current = current.children[ind]
        current.isword = True
        current.words.append(word)
    
    def findLastNode(self, word):
        current = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if(current.children[ind] == None):
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
            ind = ord(c) - ord('a')
            if(current.children[ind] == None):
               break
            current = current.children[ind] 
            i += 1
        return word[:i]
    
def main():
    words = ["abd", "abc", "ab", "def", "abcd", "xyz", "cat"]
    trie = RadixTrie()
    for word in words:
        trie.add(word)
    
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
