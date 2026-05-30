class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        left =0 
        
        for i in range(0,len(nums1)):

            while left  < len(nums2) and nums1[i]> nums2[left]:
                left+=1
            if left  < len(nums2) and nums1[i] == nums2[left]:
                return nums1[i]
        return -1