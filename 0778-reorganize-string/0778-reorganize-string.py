class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        
        pq = []
        # heapq.heapify(pq)
        for i in hashmap:
            heappush(pq,[-1*hashmap[i], i])
        # print(pq)
        s = ""
        prev = [0,"key"]
        while pq:
            k = heappop(pq)
            s+=k[1]
            k[0]+=1
            if prev[0] < 0:
                heappush(pq,prev)
            prev = k
        if len(s) == n:
            return s
        else:
            return ""


            

