class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        max_sum = 0
        min_sum = 0
        cur_sum = 0
       
        for i in range(0,len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
            min_sum = min(cur_sum,min_sum)
        return max_sum-min_sum