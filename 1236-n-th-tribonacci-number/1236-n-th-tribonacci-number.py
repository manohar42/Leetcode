class Solution:
    def tribonacci(self, n: int) -> int:

        dp = {}


        def recursion(n):
            if n in dp:
                return dp[n]
            if n == 0:
                dp[n] = 0 
                return 0
            if n == 1:
                dp[n] = 1
                return 1
            if n == 2:
                dp[n] = 1
                return 1
            dp[n] =recursion(n-1)+recursion(n-2)+recursion(n-3)

            return dp[n]
        return recursion(n)