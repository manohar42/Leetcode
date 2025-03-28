class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        new_list = list()
        n = len(grid)
        m = len(grid[0])
        # print(n,m)
        for i,j in enumerate(queries):
            new_list.append((i,j))
        new_list.sort(key = lambda x:x[1])
        res = [0]*len(queries)
        minheap = list()
        heapq.heapify(minheap)
        heappush(minheap,(grid[0][0],0,0))
        total_count = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for i in range(0,m)] for j in range(0,n)]
        visited[0][0]=True
        for query_pos,query_value in new_list:
            
            while len(minheap)>0 and minheap[0][0]<query_value:
                current_value,current_row,current_column = heappop(minheap)
                total_count+=1
                for right,left in directions:
                    next_row = current_row+right
                    next_col = current_column+left
                    # print(next_row,next_col)
                    if(next_row >=0 and next_row <n and next_col >=0 and next_col < m and
                    visited[next_row][next_col] == False):
                        visited[next_row][next_col] = True
                        heappush(minheap,(grid[next_row][next_col],next_row,next_col))
            res[query_pos] = total_count
        return res
                    

