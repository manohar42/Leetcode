class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        queue = [(0,0,0)]
        heapq.heapify(queue)
        visited = set((0,0))
        while queue:
            obstacle,i,j = heapq.heappop(queue)

            nei = [[i+1,j],[i-1,j], [i,j+1],[i,j-1]]
            
            for r,c in nei:
                if (r,c) in visited or r < 0 or r >= rows or c<0 or c>= columns:
                    continue
                visited.add((r,c))
                heapq.heappush(queue,(obstacle+grid[r][c],r,c))
                if r == rows-1 and c== columns-1:
                    return obstacle
            

