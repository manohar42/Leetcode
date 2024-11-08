class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        if n ==  1:
            return dp[1]
        # dp[2]=2

        for i in range(2,n+1):  
            count = 0
            for j in range(1,i+1):
                left = j-1
                right = i-j
                count+=(dp[left]*dp[right])
            dp[i] = count
        return dp[n]


