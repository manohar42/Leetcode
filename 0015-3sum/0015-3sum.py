class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        # print(nums)
        res = []
        for i in range(0,len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1
            while j<k:
                val = nums[i]+nums[j]+nums[k]
                # print(val,i,j,k)
                if val == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                if val > 0:
                    k-=1
                elif val < 0:
                    j+=1
        # print(res)

        return res