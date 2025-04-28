class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        i = 0 
        j = 0
        sum_value = 0
        count = 0
        while j < len(nums):
            sum_value+=nums[j]
            while i < j and sum_value *(j-i+1) >= k:
                sum_value -= nums[i]
                i+=1
            if sum_value*(j-i+1) < k:
                count+=j-i+1
            j+=1
        return count
