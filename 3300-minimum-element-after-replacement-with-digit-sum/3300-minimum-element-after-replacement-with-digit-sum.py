class Solution:
    def minElement(self, nums: List[int]) -> int:
        


        def sumofdigits(n):

            res = 0
            while n>=10:
                res+=n%10
                n=n//10
            res+=n
            return res
        min_value = float('inf')
        
        for i in range(0,len(nums)):
            nums[i] = sumofdigits(nums[i])
            if nums[i] < min_value:
                min_value=nums[i]
            
        return min_value