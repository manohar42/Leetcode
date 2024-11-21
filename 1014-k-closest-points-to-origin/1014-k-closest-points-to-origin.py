class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        queue = [] 
        heapq.heapify(queue)
        for i in points:
            length = (i[0]**2+i[1]**2)
            if len(queue) < k:
                heapq.heappush(queue,[-1*length,i[0],i[1]])
            else:
                l = heapq.heappop(queue)
                if l[0] < -1*length:
                    heapq.heappush(queue,[-1*length,i[0],i[1]])
                else:
                    heapq.heappush(queue,l)
        res = []
        while len(queue) > 0:
            l = heapq.heappop(queue)
            res.append([l[1],l[2]])
        return res



                

