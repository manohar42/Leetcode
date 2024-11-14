class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    count+=1
        timer = 0
        while queue:
            second_queue = deque()
            # print(queue)
            while queue:
                i,j = queue.popleft()
                
                if i+1 < rows and grid[i+1][j] == 1:
                    count-=1
                    grid[i+1][j] = 2
                    second_queue.append([i+1,j])

                if i-1 >= 0 and grid[i-1][j] == 1:
                    count-=1
                    grid[i-1][j] = 2
                    second_queue.append([i-1,j])

                if j+1 < columns and grid[i][j+1] == 1:
                    count-=1
                    grid[i][j+1] = 2
                    second_queue.append([i,j+1])

                if j-1 >= 0 and grid[i][j-1] == 1:
                    count-=1
                    grid[i][j-1] = 2
                    second_queue.append([i,j-1])
                # print(second_queue)
            queue = second_queue
            # print(queue)
            if len(queue) > 0:
                timer+=1
        if count != 0:
            return -1
        return timer
