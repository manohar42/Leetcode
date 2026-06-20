class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = [-1]*len(nums)
        stack = []
        for i in range(0,2*len(nums)):
            if i>= len(nums):
                i-=len(nums)
            if len(stack) == 0:
                stack.append(i)
            while len(stack)> 0 and nums[stack[-1]]<nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return res