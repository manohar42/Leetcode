class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.min_index = {}

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number
        if number in self.min_index:
            heapq.heappush(self.min_index[number],index)
        else:
            self.min_index[number] = []
            heapq.heapify(self.min_index[number])
            heapq.heappush(self.min_index[number],index)

    def find(self, number: int) -> int:
        if number in self.min_index:
            
            while len(self.min_index[number]) > 0:
                index = self.min_index[number][0]

                if self.nums[index]== number:
                    return index
                heapq.heappop(self.min_index[number])
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)