class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        negative_nums = 0
        i=0
        while i < len(nums) and nums[i] < 1:
            if nums[i] <0:
                negative_nums+=1
            i+=1
            print(i)
        return max(negative_nums,len(nums)-i)