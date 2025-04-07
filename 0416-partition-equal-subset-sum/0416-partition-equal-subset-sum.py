class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2!=0:
            return False
        sum_value = sum(nums)//2

        def recursion(nums,i,sum_value):
            if sum_value == 0:
                return True

            if i == 0:
                return False

            if nums[i-1] > sum_value:
                return recursion(nums,i-1,sum_value)
            
            return recursion(nums,i-1,sum_value-nums[i-1]) or recursion(nums,i-1,sum_value)
        
        return recursion(nums,len(nums),sum_value)
        

    
