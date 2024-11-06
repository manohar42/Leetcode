class Node:

    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next= None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.cache = {}
       self.lru = Node(0,0)
       self.mru = Node(0,0) 

       self.lru.next = self.mru
       self.mru.prev = self.lru

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # print(self.cache)
            self.remove(self.cache[key])
    
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.lru.next
            self.remove(node)
            del self.cache[node.key]
    #     self.printList(self.lru.key)

    # def printList(self,node):
        
    #     count = 0
    #     # print(self.cache)
    #     while node:
    #         count+=1
    #         print(node.key,node.val)
    #         node = node.next
    #     # print("Done", count)        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)