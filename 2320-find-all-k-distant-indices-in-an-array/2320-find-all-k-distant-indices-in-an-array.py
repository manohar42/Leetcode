class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        res = set()
        n = len(nums)
        for i in range(0,len(nums)):
            if nums[i] == key:
                left = max(0,i-k)
                right = min(n-1,abs(i+k))
                while left <= right:
                    res.add(left)
                    left+=1
        return list(res)
       