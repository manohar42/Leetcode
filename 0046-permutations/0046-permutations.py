class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        plist = []

        def permutation(nums,pos,plist):

            if pos == len(nums)-1:
                plist.append(nums.copy())
                return

            for i in range(pos,len(nums)):
                nums[i],nums[pos] = nums[pos],nums[i]
                permutation(nums,pos+1,plist)
                nums[i],nums[pos] = nums[pos],nums[i]
            
        permutation(nums,0,plist)
        return plist        
