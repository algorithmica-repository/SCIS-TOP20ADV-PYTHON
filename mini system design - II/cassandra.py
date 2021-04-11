import sys
from collections import OrderedDict
import random

class Entry():
    def __init__(self, ts=-1, val=""):
        self.ts = ts
        self.val = val
    def __repr__(self):
        return str(self.ts) + "," + self.val
    
class MiniCassandra():
    def __init__(self):
        self.store = {}
        
    def put(self, key, value, ts):
        user_messages = self.store.get(key)
        if(user_messages == None):
            user_messages = OrderedDict()
            self.store[key] = user_messages
        user_messages[ts] = value
    
    def get(self, key, ts):
        user_messages = self.store.get(key)
        if(user_messages == None):
            return None
        res = Entry()
        for key, value in user_messages.items():
            if key <= ts:
                res = Entry(key, value)
        return res
        
    def query(self, key, ts_start, ts_end):
        user_messages = self.store.get(key)
        if(user_messages == None):
            return None
        res = []
        for ts, value in user_messages.items():
            if ts >= ts_start and ts <= ts_end:
                res.append(Entry(ts, value))
        return res    

    def display(self):
        print(self.store)

def main():
    cassandra = MiniCassandra()
    for ts in range(20):
        rid = random.randint(0, 4)
        cassandra.put("user"+str(rid), "message"+str(rid), ts)
    cassandra.display()
    
    for i in range(5):
        rid = random.randint(0, 4)
        rts = random.randint(0,25)
        print("user"+str(rid), rts)
        print(cassandra.get("user"+str(rid), rts))

    for i in range(5):
        rid = random.randint(0, 4)
        print("user"+str(rid)+"(5-10)")
        print(cassandra.query("user"+str(rid), 5, 10))
    
if __name__=="__main__":
    main()
