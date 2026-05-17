class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answers = set()
        result = []
        for i in range(0,len(nums)):
            left = i+1
            right = len(nums)-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                # print(i,left,right)
                if nums[i]+nums[left]+nums[right] == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                    
                    right-=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left+=1
                else:
                    right-=1
        return result


