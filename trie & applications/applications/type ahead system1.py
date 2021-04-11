import sys

class TypeAheadSystem1():
    def __init__(self):
        self.index = {}
    
    def build(self, names):
        for name in names:
            for i in range(0, len(name)):
                for j in range(i+1, len(name)+1):
                    key = name[i:j]
                    #print(key)
                    if(self.index.get(key) == None):
                        self.index[key] = set()
                    self.index[key].add(name)
    
    def display(self):
        print(self.index)
    
    def query(self, text):
        if(self.index.get(text) == None):
            return None
        res = []
        for e in self.index[text]:
            res.append(e)
        return res

def main():
    names = ["krishna", "jesus", "yoga", "lord", "karma yoga", "bhakti yoga"]
    system = TypeAheadSystem1()
    system.build(names)
    system.display()
    print(system.query(sys.argv[1]))
    
if __name__=="__main__":
    main()
