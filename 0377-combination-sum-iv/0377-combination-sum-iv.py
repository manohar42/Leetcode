class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        nums.sort()
        memo = {}
       
        def recursion(n):
            if n in memo:
                return memo[n]
            if n ==0:
                return 1
            if n < nums[0]:
                return 0
            
            count = 0
            for i in range(0,len(nums)):
                if n-nums[i] < 0:
                    break
                count+=recursion(n-nums[i])
            memo[n]= count
            return count    
       
        return recursion(target)