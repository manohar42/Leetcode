class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # if sum(nums)%2!=0:
        #     return False
        # sum_value = sum(nums)//2
        # dp = set()
        # dp.add(0)

        # def recursion(nums,dp,i):
        #     if index == -1:
        #         return False
        #     sub_dp = set()
        #     for t in dp:
        #         sub_dp.add(t+nums[i])
        #         sub_dp.add(t)
        #         if t+nums[i]== sum_value:
        #             return True
        #     dp = sub_dp
        #     return recursion(nums,dp,i-1)
            
        # return recursion(nums,dp,len(nums)-1)
        if sum(nums)%2 != 0:
            return False
        dp = set()
        dp.add(0)

        n =len(nums)-1
        target = sum(nums)//2
        def recursion(nums,dp,index):

            if index == -1:
                return False
            
            sub_dp = set()
            for t in dp:
                sub_dp.add(t+nums[index])
                sub_dp.add(t)
                if t+nums[index] == target:
                    return True
            dp = sub_dp
            return recursion(nums,dp,index-1)



        
        return recursion(nums,dp,n)
