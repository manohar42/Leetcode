class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        array = [0]*len(nums)
        n = len(nums)
        for i in queries:
            left,right = i[0],i[1]
            array[left] -=1
            if right+1 < n:
                array[right+1] +=1
        val = 0
        for i in range(0,len(nums)):
            val += array[i]
            if val + nums[i]<=0:
                continue
            else:
                return False
        return True
                
                
                