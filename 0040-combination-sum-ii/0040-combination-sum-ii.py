class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        sol = []
        n = len(candidates)
        if sum(candidates) < target:
            return []
        def backtrack(i,cur):
            if sum(cur[:]) == target:
                res.append(cur[:])
                return
            if sum(cur[:]) > target or i==n:
                return
            
            cur.append(candidates[i])
            backtrack(i+1, cur)
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i=i+1
            backtrack(i+1,cur)
                
            


           
        backtrack(0,[])
        return sorted(res)