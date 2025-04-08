class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_value = -1
        nums.sort()
        num_set = set()
        count = 0
        for i in range(0,len(nums)):
            if nums[i] <= max_value:
                count+= max_value - nums[i]+1
                nums[i]= max_value+1
            max_value = max(max_value,nums[i])
        return count
