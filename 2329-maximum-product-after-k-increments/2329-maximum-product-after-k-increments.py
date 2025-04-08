class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod= 10**9+7
        queue = list()
        heapq.heapify(nums)
        
        while k > 0:
            value = heapq.heappop(nums)
            heapq.heappush(nums,value+1)
            k-=1
        value = 1
        for i in nums:
            value*=i
            value = value%mod
        return value



        