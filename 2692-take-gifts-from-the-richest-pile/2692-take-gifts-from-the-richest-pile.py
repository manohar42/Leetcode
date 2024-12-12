class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        stack = []
        heapify(stack)
        No_of_gifts = 0
        n = len(gifts)
        for i in range(n):
            No_of_gifts+= gifts[i]
            heappush(stack,-1*gifts[i])
        while k > 0:
            p = -1*heappop(stack)
            No_of_gifts -=p
            p = math.floor(sqrt(p))
            No_of_gifts+=p
            heappush(stack, -1*p)
            k-=1
        return No_of_gifts

