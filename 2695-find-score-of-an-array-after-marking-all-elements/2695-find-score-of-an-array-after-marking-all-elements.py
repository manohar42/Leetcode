class Solution:
    def findScore(self, nums: List[int]) -> int:

        queue =[]
        heapq.heapify(queue)
        n = len(nums)
        for i in range(n):
            heapq.heappush(queue,(nums[i],i))
        marked = [False]*n
        marked_sum = 0
        while queue:
            value,index = heapq.heappop(queue)
            if marked[index] == False:
                marked[index] = True
                if index-1>=0 and marked[index-1] == False:
                    marked[index-1] = True
                if index+1 <n and marked[index+1] == False:
                    marked[index+1]= True
                marked_sum+=(value)
                # print(value)
        return marked_sum
                
            
            
