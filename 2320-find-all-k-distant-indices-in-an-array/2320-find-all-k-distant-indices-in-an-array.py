class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        res = set()
        sub = []
        for i in range(0,len(nums)):
            if nums[i] == key:
                sub.append(i)
        n = len(nums)
        i = 0
        for i in sub:       
            left = max(0,i-k)
            right = min(n-1,abs(i+k))
            while left <= right:
                res.add(left)
                left+=1
        return list(res)