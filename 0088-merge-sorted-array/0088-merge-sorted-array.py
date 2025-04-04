class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        a= m-1
        b = n-1

        while m+n > 0 and n > 0:
            if nums1[m-1] > nums2[n-1] and (m-1) >= 0:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        return nums1
        