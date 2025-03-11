class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def distinct_count(nums,k):
            nums_count = 0
            start = 0
            end = 0
            distinct_nums = {}
            n = len(nums)
            while end < n:
                distinct_nums[nums[end]] = distinct_nums.get(nums[end],0)+1

                if len(distinct_nums) <=k:
                    nums_count+=end-start+1
                else:
                    while len(distinct_nums) > k:
                        distinct_nums[nums[start]] = distinct_nums.get(nums[start],0)-1
                        if distinct_nums[nums[start]] == 0:
                            del distinct_nums[nums[start]]
                        start+=1
                    if len(distinct_nums) <=k:
                        nums_count+=end-start+1
                end+=1
            return nums_count
        return distinct_count(nums,k)- distinct_count(nums,k-1)