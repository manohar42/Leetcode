class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heaplist = []
        heapq.heapify(heaplist)
        for i in range(0,len(nums)):
            heapq.heappush(heaplist,[nums[i],i])
            if len(heaplist)>k:
                heapq.heappop(heaplist)
        res = []
        while len(heaplist):
            res.append(heapq.heappop(heaplist))
        res.sort(key=lambda x:x[1])
        
        return [val for val,idx in res]

