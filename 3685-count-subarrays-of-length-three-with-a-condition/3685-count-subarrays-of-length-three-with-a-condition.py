class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        right = 2
        count = 0
        for i in range(0,len(nums)-2):
            if (nums[i]+nums[right])*2 == nums[i+1]:
                count+=1
            right+=1
        return count 