class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res= []
        for i in range(0,n,3):
            # print(nums[i],nums[i+1],nums[i+2])
            if abs(nums[i]-nums[i+1]) <=k and abs(nums[i+1]-nums[i+2])<=k and abs(nums[i+2]-nums[i]) <= k:
                res.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
        return res