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
            while i < n:
                if nums[i] == key:
                    left = max(0,i-k)
                    right = min(n-1,abs(i+k))
                    # print(left,right)
                    while left <= right:
                        res.add(left)
                        left+=1
                    i = right+1
                else:
                    i+=1
        return list(res)