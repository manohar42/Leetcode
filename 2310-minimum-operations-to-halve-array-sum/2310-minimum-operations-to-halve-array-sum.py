class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        array_sum = sum(nums)
        k = (array_sum)/2
        heap_nums = []
        heapify(heap_nums)
        for i in nums:
            heappush(heap_nums,-i)
        operations = 0
        while k < array_sum:
            operations+=1
            x = -1*heappop(heap_nums)
            x = x/2
            array_sum-=x
            heappush(heap_nums,-x)
        return operations