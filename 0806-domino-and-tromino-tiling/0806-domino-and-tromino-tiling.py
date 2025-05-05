class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        if n == 1:
            return 1
        
        dp = [ 0 for i in range(0,n+1)]
        # print(dp)
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = (dp[i-1]*2+dp[i-3])%mod
        # print(dp)
        return dp[n]%mod