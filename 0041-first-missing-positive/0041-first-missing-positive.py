class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)

        for i in range(1,len(nums)+2):
            if i not in set_nums:
                return i
