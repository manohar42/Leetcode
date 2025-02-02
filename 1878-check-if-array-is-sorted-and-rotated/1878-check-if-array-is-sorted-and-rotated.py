class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                       break
            i+=1
        # print(nums[i:]+nums[:i])     
        return sorted(nums) == nums[i:]+nums[:i]