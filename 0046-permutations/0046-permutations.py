class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [False]*len(nums)
        result = []
        def backtrack(start,current):

            if len(current) == len(nums):

                result.append(current[:])
                return
            
            for i in range(0,len(nums)):
                if visited[i] == True:
                    continue
                else:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack(start,current)
                    current.pop()
                    visited[i] = False
        backtrack(0,[])
        return result