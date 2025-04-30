class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        nums.sort()
        value = 10
        digit = 1
        count = 0
        for i in range(0,len(nums)):

            while nums[i] >= value:
                value *= 10
                digit+=1
            if digit%2 == 0:
                count+=1
        return count