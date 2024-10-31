class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        
        def recursion(m,n):
            if dp[m][n] != -1:
                return dp[m][n]
            if m <0 or n<0:
                return float('inf')
                
            if m ==0 and n == 0:
                return grid[m][n]
            
            dp[m][n] = grid[m][n] + min(recursion(m-1,n), recursion(m,n-1))

            return dp[m][n]
            
        
        return recursion(m-1,n-1)