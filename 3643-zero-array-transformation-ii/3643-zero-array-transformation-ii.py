class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def check_count(nums,queries,mid):
            
            difference_array = [0]*(len(nums)+1)

            for i in range(mid):
                start,end,val = queries[i]
                difference_array[start] +=val
                difference_array[end+1] -= val
            prefix_sum = 0

            for i in range(len(nums)):
                prefix_sum+=difference_array[i]
                if prefix_sum < nums[i]:
                    return False
            return True
        if not check_count(nums,queries,len(queries)):
            return -1
        left = 0
        right = len(queries)

        while left<=right:

            mid = left+(right-left)//2

            if check_count(nums,queries,mid):
                right=mid-1
            else:
                left = mid+1
        
        return left