class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        zero_count_1 = 0
        zero_count_2 = 0
        for i in nums1:
            if i == 0:
                zero_count_1+=1
        
        for i in nums2:
            if i == 0:
                zero_count_2+=1
        if zero_count_1 == 0 and sum(nums1) < sum(nums2)+zero_count_2:
            return -1
        elif zero_count_2 == 0 and sum(nums2) < sum(nums1)+zero_count_1:
            return -1
        else:
            return max(sum(nums1)+zero_count_1,sum(nums2)+zero_count_2)

            
