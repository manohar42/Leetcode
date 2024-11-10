class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        def dfs(i,j):
            length = 0
            if i<0 or i> rows-1 or j < 0 or j > columns-1:
                return 0
            else:
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    length =1+ dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1)
            return length

        max_length = 0
        present_length = 0
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j] == 1:
                    present_length = dfs(i,j)
                max_length = max(present_length,max_length)
        return max_length
