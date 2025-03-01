class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = []
        for i in range(0,n):
            if i < n-1 and nums[i] == nums[i+1] and nums[i]!= 0:
                res.append(nums[i]*2)
                nums[i+1]= 0
            elif nums[i] > 0:
                res.append(nums[i]) 
        count = len(res)

        for i in range(0,n-count):
            res.append(0)
        return res