class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        right = 0
        count = 0
        max_value = max(nums)
        max_count = 0
        n = len(nums)
        for i in range(0,n):
            if i > 0:
                if nums[i-1] == max_value:
                    max_count-=1
            while right < n and max_count < k:
                if nums[right] == max_value:
                    max_count+=1
                right+=1
            if max_count == k:
                count+= n-right+1
        return count
        