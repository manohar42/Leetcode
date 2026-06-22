class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)
    
    def transfer(self):
        if len(self.stackB) == 0:
            while len(self.stackA) >0:
                self.stackB.append(self.stackA.pop())
    def pop(self) -> int:
        self.transfer()
        return self.stackB.pop()

    def peek(self) -> int:
        self.transfer()
        return self.stackB[-1]

    def empty(self) -> bool:
        if len(self.stackA) == 0 and len(self.stackB)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()