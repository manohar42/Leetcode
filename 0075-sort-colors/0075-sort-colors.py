class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {0:0,1:0,2:0}
        for i in range(0,len(nums)):
            hashmap[nums[i]]+=1
        j = 0
        for i in hashmap:
            while hashmap[i] > 0:
                nums[j] = i
                hashmap[i]-=1
                j+=1