class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        count = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=nums[i]
            else:
                count = nums[i]
            max_sum = max(max_sum,count)
        return max_sum