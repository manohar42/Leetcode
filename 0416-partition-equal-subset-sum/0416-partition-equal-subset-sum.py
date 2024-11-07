class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        # if sum(nums)%2 != 0:
        #     return False
        # dp = set()
        # dp.add(0)

        # n =len(nums)-1
        # target = sum(nums)//2

        # for i in range(n,-1,-1):
        #     next_dp = set()
        #     for j in dp:
        #         next_dp.add(j+nums[i])
        #         next_dp.add(j)
        #         if j == target:
        #             return True
        #     dp = next_dp
        
        # return False

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

