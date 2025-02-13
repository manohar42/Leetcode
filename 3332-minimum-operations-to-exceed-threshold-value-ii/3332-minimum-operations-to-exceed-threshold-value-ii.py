class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap_nums = nums
        heapq.heapify(heap_nums)
        operations = 0
        while True:
            x = heappop(heap_nums)
            if x >= k:
                heappush(heap_nums,x)
                break
            operations+=1
            y = heappop(heap_nums)
            z = x*2 + y
            heappush(heap_nums,z)
        return operations
