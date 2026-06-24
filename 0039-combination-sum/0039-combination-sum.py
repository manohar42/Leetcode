class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(start,curr):

            if sum(curr) == target:
                result.append(curr[:])
                return
            elif sum(curr) > target:
                return
            else:
                for i in range(start,len(candidates)):
                    curr.append(candidates[i])
                    backtrack(i,curr)
                    curr.pop()

        backtrack(0,[])
        return result

