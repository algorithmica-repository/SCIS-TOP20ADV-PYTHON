import sys
from radixtrie import RadixTrie

class TypeAheadSystem2():
    def __init__(self):
        self.index = RadixTrie()
    
    def build(self, names):
        for name in names:
            for i in range(0, len(name)):
                    key = name[i:]
                    #print(key)
                    self.index.add(key, name)
    
    def display(self):
        print(self.index.startsWith(""))
    
    def query(self, text):
        return self.index.startsWith(text)

def main():
    names = ["krishna", "jesus", "yoga", "lord", "karma yoga", "bhakti yoga"]
    system = TypeAheadSystem2()
    system.build(names)
    system.display()
    print(system.query(sys.argv[1]))
    
if __name__=="__main__":
    main()
