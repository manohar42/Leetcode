class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res,sol = [],[]
        n = len(candidates)
        def backtrack(index):
            
            if sum(sol) == target:
                res.append(sol[:])
                return
            elif sum(sol) > target:
                return
            
            for i in range(index,n):
                sol.append(candidates[i])
                backtrack(i)
                sol.pop()
        
        backtrack(0)
        return res