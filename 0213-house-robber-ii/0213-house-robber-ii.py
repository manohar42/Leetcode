class Solution:
    def rob(self, nums: List[int]) -> int:
        

        n = len(nums)

        dp = [0]*n

        dp_1 = [0]*n

        if len(dp) == 1:
            return nums[0]
        if n <= 3:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(dp[1], dp[0]+nums[2])

        dp_1[1] = nums[1]
        dp_1[2] = max(nums[1],nums[2])

        for i in range(3,n-1):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
            dp_1[i] = max(dp_1[i-1], dp_1[i-2]+nums[i])
        
        dp_1[n-1] = max(dp_1[n-2],dp_1[n-3]+nums[n-1])
        return max(dp[n-2], dp_1[n-1])