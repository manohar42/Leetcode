class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        duplicate = -1
        n = len(nums)
        missing = 1
        for i in range(0,len(nums)):
            target_index = abs(nums[i])-1

            if nums[target_index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[target_index]= -nums[target_index]
        
        for i in range(n):
            if nums[i] > 0:
                missing = i+1
        return [duplicate,missing]
