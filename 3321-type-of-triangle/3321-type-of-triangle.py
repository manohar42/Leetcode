class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        k = max(nums)
        # print(k,sum(nums))
        if (sum(nums)- k) <= k:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"