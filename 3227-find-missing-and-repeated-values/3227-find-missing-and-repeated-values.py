class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

       
        n = len(grid)
        sum_value = ((n**2)*((n**2)+1))//2
        # print(sum_value)
        values_set = set()
        duplicate_value = 0
        for i in range(0,n):
            for j in range(0,n):
                if grid[i][j] in values_set:
                    duplicate_value = grid[i][j]
                    continue
                sum_value-=grid[i][j]
                values_set.add(grid[i][j])
        return [duplicate_value, sum_value]
