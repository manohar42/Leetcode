class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        res1 = []
        res2 = []
        pivot_count = 0
        for i in range(0,len(nums)):
            if nums[i] < pivot:
                res1.append(nums[i])
            elif nums[i] > pivot:
                res2.append(nums[i])
            else:
                pivot_count+=1
        
        return res1+[pivot]*pivot_count+res2