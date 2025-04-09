class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        min_value = min(nums)
        if k > min_value:
            return -1
        nums.sort()
        count = 0
        # print(nums)
        for i in range(len(nums)-1,0,-1):
            # print(nums[i],nums[i-1])
            if nums[i] != nums[i-1]:
                count+=1
        
        if min_value == k:
            return count
        return count+1
            