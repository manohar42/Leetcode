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
            # print(res)
        # print(res)
        res.sort(key=lambda x:x[1])
        # print(res)
        return [idx for idx,val in res]

