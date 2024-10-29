class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        k = max(cost)
        dp = [k]*n

        if len(cost) == 1:
            return nums[0]

        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for i in range(n-3,-1,-1):
            dp[i] = min(dp[i+1],dp[i+2])+cost[i]
        
        return min(dp[0],dp[1])