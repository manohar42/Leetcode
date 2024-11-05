class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]


        def recursion(s1,s2,m,n):

            if m == 0:
                return n
            if n == 0:
                return m

            if dp[m-1][n-1] != -1:
                return dp[m-1][n-1]

            if s1[m-1] == s2[n-1]:
                dp[m-1][n-1] = recursion(s1,s2,m-1,n-1)
            else:
                dp[m-1][n-1] =  1+min(recursion(s1,s2,m,n-1), recursion(s1,s2,m-1,n), recursion(s1,s2,m-1,n-1))
            return dp[m-1][n-1]
        
        return recursion(word1,word2,len(word1),len(word2))
