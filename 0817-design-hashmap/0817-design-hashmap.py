class Node:
    def __init__(self,key,value,next = None):
        self.key = key
        self.value = value
        self.next = next
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None]*self.size
    def hashing(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        
        index = self.hashing(key)
        if self.table[index] is None:
            self.table[index] = Node(key,value)
            return 
        
        current = self.table[index]
        # print("In put",current.key)
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next == None:
                current.next = Node(key,value)
                return 
            current = current.next


    def get(self, key: int) -> int:

        index = self.hashing(key)
        # print(index)
        if self.table[index] is None:
            # print(key)
            return -1
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            if current.next == None:
                return -1
            current = current.next       

    def remove(self, key: int) -> None:
        index = self.hashing(key)
        if self.table[index] is None:
            return 
        current = self.table[index]
        # print(current.key)
        if current.key == key:
            self.table[index] = current.next
            # print(current.next.key)
            return
        
        while current:
            if current.key == key:
                # print(prev.)
                # if current.next is None:
                #     prev.next = None
                #     return
                prev.next = current.next
                return
            prev = current
            if current.next is None:
                return
            current = current.next
            
            



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)