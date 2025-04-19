class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:


        def helper(val):
            right = len(nums)-1
            count = 0
            for i in range(0,len(nums)):
                while i<right and nums[i]+nums[right] > val:
                   right-=1
                count+=max(0,right-i)


            return count


        nums.sort()
        return helper(upper)-helper(lower-1)
        