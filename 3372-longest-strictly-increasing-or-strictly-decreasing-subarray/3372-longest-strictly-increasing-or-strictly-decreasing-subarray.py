class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        i_count = 1
        d_count = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] :
                i_count +=1
                d_count = 1
            elif nums[i-1] > nums[i]:
                d_count +=1
                i_count = 1
            else:
                d_count = 1
                i_count = 1
            # print(nums[i],d_count,i_count)
            count = max(count,i_count,d_count)
        return count
            