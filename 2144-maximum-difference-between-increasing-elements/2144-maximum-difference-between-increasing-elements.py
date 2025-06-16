class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        min_val = nums[0]
        max_diff = -1
        for i in range(1,len(nums)):
    
            if nums[i] > min_val:
                diff = nums[i] - min_val
                max_diff = max(max_diff,diff)
            else:
                min_val = min(min_val,nums[i])
        return max_diff
            