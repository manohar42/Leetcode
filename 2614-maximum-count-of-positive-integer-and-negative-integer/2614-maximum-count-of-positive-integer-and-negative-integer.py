class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        negative_nums = 0
        i=0
        while i < len(nums) and nums[i] < 0:
            negative_nums+=1
            i+=1
            print(i)
        while i < len(nums) and nums[i] == 0:
            i+=1
            continue
        return max(negative_nums,len(nums)-i)