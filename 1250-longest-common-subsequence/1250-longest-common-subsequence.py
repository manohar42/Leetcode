class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
       
        m = len(s1)
        n = len(s2)
        sequence =[[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        
        def dp(s1,s2,m,n):
            
            if m == 0 or n == 0:
                return 0
            # print(s1[m-1], s2[n-1], sequence[m][n])
            if sequence[m][n]!= -1:
                return sequence[m][n]

            if s1[m-1] == s2[n-1]:
                sequence[m][n] = 1 + dp(s1,s2, m-1, n-1)
            else:
                sequence[m][n] = max(dp(s1,s2,m-1,n), dp(s1,s2,m,n-1))
            return sequence[m][n]
        
        return dp(s1,s2,m,n)

        