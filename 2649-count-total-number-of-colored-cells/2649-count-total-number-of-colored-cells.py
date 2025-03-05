class Solution:
    def coloredCells(self, n: int) -> int:

        row_count = n*2-1
        number_of_colored_cells= 0
        for i in range(row_count-2,-1,-2):
            number_of_colored_cells+=i

        return number_of_colored_cells*2+row_count


