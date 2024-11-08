class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if sum(nums) < target:
            return 0
       
        n = len(nums)
        memo = {}
        def recursion(nums,cur_sum,target,n):

            if cur_sum ==  target and n == 0:
                return 1
            if (n, cur_sum) in memo:
                return memo[(n, cur_sum)]
            if n < 0:
                return 0
            memo[(n, cur_sum)] = recursion(nums,cur_sum+nums[n-1],target, n-1) + recursion(nums,cur_sum-nums[n-1],target,n-1)

            return memo[(n, cur_sum)]
           
        return recursion(nums,0,target, n)