class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = []
        left = 0
        right = 1
        n = len(nums)
        while right < n:
            if nums[right] - nums[left] <=k:
                right+=1
            else:
                res.append(nums[left:right])
                left = right
        if left!= right:
            res.append(nums[left:])
        return len(res)
