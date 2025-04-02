class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left = [0] *len(nums)
        right = [0]*len(nums)
        left[0] = nums[0]
        right[-1]= nums[-1]
        for i in range(1,len(nums)):
            left[i] = max(nums[i],left[i-1])
        for j in range(len(nums)-2,-1,-1):
            right[j] = max(nums[j],right[j+1])
        max_value = 0
        for i in range(1,len(nums)-1):
            value = (left[i-1]-nums[i])*right[i+1]
            max_value = max(value,max_value)
    
        return max_value
