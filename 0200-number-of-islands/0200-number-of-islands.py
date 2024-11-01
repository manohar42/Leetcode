class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        def dfs(i,j):
            if (i<0 or i> m-1 or j<0 or j>n-1) or grid[i][j] != "1":
                return
            else:
                grid[i][j]= "0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(0,m):
            for j in range(0,n):                
                if grid[i][j] == "1":
                    dfs(i,j)
                    # while queue:
                        # row,column =queue.popleft()
                        # grid[row][column] = "0"
                        # if 0 <= (row+1) <= m-1 and grid[row+1][column] == "1":
                        #     queue.append([row+1, column])
                        # if 0<= (column+1) <= n-1 and grid[row][column+1] == "1":
                        #     queue.append([row, column+1])
                        # if 0 <= (row-1) <= m-1 and grid[row-1][column] == "1":
                        #     queue.append([row-1, column])
                        # if 0<= (column-1) <= n-1 and grid[row][column-1] == "1":
                        #     queue.append([row, column-1])
                        # # print(queue)

                        
                    count+=1
        return count
                
    

