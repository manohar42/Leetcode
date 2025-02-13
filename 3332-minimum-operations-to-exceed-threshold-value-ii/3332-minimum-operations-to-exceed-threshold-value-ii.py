class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        operations = 0
        while True:
            x = heappop(nums)
            if x >= k:
                return operations
            operations+=1
            y = heappop(nums)
            z = x*2 + y
            heappush(nums,z)