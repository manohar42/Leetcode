class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        stack = []
        
        n = len(nums)
        for i in range(n):
            stack.append((nums[i],i))
        heapq.heapify(stack)
        while k>0:
            value,index = heapq.heappop(stack)
            value = value*multiplier
            nums[index] = value
            heapq.heappush(stack,(value,index))
            k-=1
        return nums
