class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        stack = []
        heapify(stack)

        for i in nums:
            heapq.heappush(stack,i)
            if len(stack) > k:
                heapq.heappop(stack)       
        return stack[0]