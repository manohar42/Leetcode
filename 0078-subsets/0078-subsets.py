class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(subsets, nums, index):
    
            res.append(subsets[:])
            
            for i in range(index,len(nums)):
                subsets.append(nums[i])
                backtrack(subsets,nums,i+1)            
                subsets.pop()

        backtrack([], nums,0)

        return res 