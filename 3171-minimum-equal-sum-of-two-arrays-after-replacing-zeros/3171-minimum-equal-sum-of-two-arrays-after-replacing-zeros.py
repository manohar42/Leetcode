class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        zero_count_1 = 0
        zero_count_2 = 0
        sum_1 = sum(nums1)
        sum_2 = sum(nums2)
        for i in nums1:
            if i == 0:
                zero_count_1+=1
        
        for i in nums2:
            if i == 0:
                zero_count_2+=1
        if (zero_count_1 == 0 and sum_1 < sum_2+zero_count_2) or (zero_count_2 == 0 and sum_2 < sum_1+zero_count_1):
            return -1
        else:
            return max(sum_1+zero_count_1,sum_2+zero_count_2)

            
