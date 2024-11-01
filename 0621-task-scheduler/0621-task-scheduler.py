class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = Counter(tasks)
        count = [-1*i for i in c.values()]
        heapq.heapify(count)

        q = deque()
        time = 0

        while count or q:
            time+=1

            if count:
                k = heapq.heappop(count)
                if k+1 < 0:
                    q.append([k+1,time+n])

            if q and q[0][1] == time:
                heapq.heappush(count, q.popleft()[0])
        return time
                
