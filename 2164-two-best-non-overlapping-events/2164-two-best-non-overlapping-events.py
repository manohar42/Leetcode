class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        heap = []
        heapify(heap)
        res1,res2 = 0,0
        for start, end, value in events:
            while heap and heap[0][0] < start:
                res1 = max(res1,heapq.heappop(heap)[1])
            res2 = max(res2,res1+value)
            heapq.heappush(heap,(end,value))
        return res2 