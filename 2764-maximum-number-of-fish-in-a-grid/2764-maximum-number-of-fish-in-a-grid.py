class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        

        visited = set()
        def dfs(i,j,fishes):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            fishes += grid[i][j]
            fishes += dfs(i+1,j,0)+dfs(i,j+1,0)+dfs(i-1,j,0)+dfs(i,j-1,0)
            return fishes
        m = len(grid)
        n = len(grid[0])
        max_fishes = 0
        for i in range(m):
            for j in range(n):
                visited = set()
                if grid[i][j] != 0:
                    max_fishes = max(max_fishes,dfs(i,j,0))
                    
        return max_fishes