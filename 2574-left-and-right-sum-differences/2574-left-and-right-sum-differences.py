class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        answer = [0]*len(nums)
        for i in range(0,len(nums)):
            answer[i] = abs(right_sum-nums[i]-left_sum)
            right_sum-=nums[i]
            left_sum+=nums[i]
        
        return answer