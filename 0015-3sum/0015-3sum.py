class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output_list = []
        nums.sort()
        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                ThreeSum = nums[i]+nums[left]+nums[right]
                if ThreeSum == 0:
                    k = [nums[i], nums[left], nums[right]]
                    if k not in output_list:
                        output_list.append(k)
                    left+=1
                    right-=1
                elif ThreeSum < 0:
                    left+=1
                else:
                    right-=1
                
        return output_list
