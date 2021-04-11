import random

class DListNode():
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = self
        self.next = self
        
class DoublyLinkedList():
    def __init__(self):
        self.head = DListNode()
        self.sz = 0
        
    def size(self):
        return self.sz
    
    def removeFirst(self):
        first = self.head.next
        first.next.prev = self.head
        self.head.next = first.next
        self.sz -= 1
        return first
    
    def addLast(self, key, val):
        tmp = DListNode(key, val)
        tmp.next = self.head
        tmp.prev = self.head.prev
        self.head.prev.next = tmp
        self.head.prev = tmp
        self.sz += 1
        return tmp
        
    def removeAndAddLast(self, tmp):
        #unlink
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        #add at last position
        tmp.next = self.head
        tmp.prev = self.head.prev
        self.head.prev.next = tmp
        self.head.prev = tmp
        
    def display(self):
        current = self.head.next
        while(current != self.head):
            print("(" + current.key + "," + current.val + ")", end=",")
            current = current.next
        print()
        
class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoublyLinkedList()
        
    #TC:O(1)
    def put(self, key, val):
        tmp = self.map.get(key)
        if(tmp != None):
            tmp.val = val
        else:
           if(self.capacity == self.list.size()):
               lruNode = self.list.removeFirst()
               self.map.pop(lruNode.key)
           lastNode = self.list.addLast(key, val)
           self.map[key] = lastNode
           
    #TC:O(1)
    def get(self, key):
        tmp = self.map.get(key)
        if(tmp == None):
           return None
        self.list.removeAndAddLast(tmp)        
        return tmp.val
    
    def display(self):
        self.list.display()               

def main():
    cache = LRUCache(3)
    for i in range(20):
        cache.put("key"+str(i), "val"+str(i))
        cache.display()
    for i in range(5):
        rkey = "key"+ str(random.randint(0, 19))
        print(rkey)
        print(cache.get(rkey))
        cache.display()
    
if __name__=="__main__":
    main()
