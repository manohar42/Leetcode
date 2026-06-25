class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(start,value,curr):

            if value == target:
                result.append(curr[:])
                return
            elif value > target:
                return
            else:
                for i in range(start,len(candidates)):
                    if candidates[i] > target:
                        continue
                    value+=candidates[i]
                    curr.append(candidates[i])
                    backtrack(i,value,curr)
                    curr.pop()
                    value-=candidates[i]

        backtrack(0,0,[])
        return result

