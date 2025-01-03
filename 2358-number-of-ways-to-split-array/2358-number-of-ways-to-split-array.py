class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        count_left  = 0
        count_right = sum(nums)
        count = 0
        n = len(nums)
        for i in range(0,n-1):
            count_left+=nums[i]
            count_right-=nums[i]
            if count_left >= count_right:
                count+=1
        return count
