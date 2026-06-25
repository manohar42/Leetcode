class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        def backtrack(start,curr):

            result.append(curr[:])

            for i in range(start,n):

                if i > start and nums[i] == nums[i-1]:
                    continue
                
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        
        backtrack(0,[])
        return result
