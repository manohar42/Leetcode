class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        n = len(nums)
        def backtrack(curr,counter):

            if len(curr) == n:
                result.append(curr[:])
                return
            
            for num in counter:

                if counter[num] > 0:

                    curr.append(num)
                    counter[num]-=1
                    backtrack(curr,counter)
                    counter[num]+=1
                    curr.pop()
                
                
        backtrack([],Counter(nums))

        return result



