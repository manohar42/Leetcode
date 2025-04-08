class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        hashmap = {}

        for i in range(len(nums)-1,-1,-1):

            if nums[i] in hashmap:
                return i//3+1
            hashmap[nums[i]] = i
        return 0