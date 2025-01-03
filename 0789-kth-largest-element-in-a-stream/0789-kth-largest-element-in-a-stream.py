class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.nums = nums
        # print(self.nums)
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        return 
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        else :
            heapq.heappush(self.nums,val)
            heapq.heappop(self.nums)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)