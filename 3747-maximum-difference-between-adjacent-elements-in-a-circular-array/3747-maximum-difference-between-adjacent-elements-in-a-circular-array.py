class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        max_diff = 0

        nums.append(nums[0])
        for i in range(1,len(nums)):
            if max_diff < abs(nums[i-1]-nums[i]):
                max_diff = abs(nums[i-1]-nums[i])
        return max_diff