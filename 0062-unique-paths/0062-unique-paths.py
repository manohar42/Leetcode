class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        paths = [[0 for _ in range(n+1)] for _ in range(m+1)]

        def dp(a,b):
            
            if a == m or b == n:
                return 0
            if paths[a][b] != 0:
                return paths[a][b]
            # if a*b == m*n:
            #     return paths[0][0]
            else:
                paths[a][b] = 1+dp(a+1,b)+dp(a,b+1)

            return paths[a][b]
        
        
        end = m*n
        d = dp(0,0)

        return paths[1][1]+1

