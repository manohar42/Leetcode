class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        answer = [0]*len(nums)
        for i in range(0,len(nums)):
            right_sum-=nums[i]
            answer[i] = abs(right_sum-left_sum)
            left_sum+=nums[i]
        
        return answer