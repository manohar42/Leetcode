class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def countvalues(val):
            j = len(nums)-1
            # print(nums)
            res = 0
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0,j-i)
            return res
        
        nums.sort()

        print(countvalues(upper))
        print(countvalues(lower-1))
        return countvalues(upper) - countvalues(lower-1)