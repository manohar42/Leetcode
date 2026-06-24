class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start,value,curr):

            if value == target:
                result.append(curr[:])
            elif value > target:
                return
            else:
                for i in range(start,len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if candidates[i] > target:
                        return
                    curr.append(candidates[i])
                    value+=candidates[i]
                    backtrack(i+1, value, curr)
                    curr.pop()
                    value-=candidates[i]
                    


        backtrack(0,0,[])
        return result

