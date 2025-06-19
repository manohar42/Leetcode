class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        count = 0
        left = 0
        right = 1
        n = len(nums)
        while right < n:
            if nums[right] - nums[left] <=k:
                right+=1
            else:
                count+=1
                left = right
        if left!= right:
            count+=1
        return count
