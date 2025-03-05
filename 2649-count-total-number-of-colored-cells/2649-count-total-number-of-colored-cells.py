class Solution:
    def coloredCells(self, n: int) -> int:

        row_count = n*2-1
        colored_rows = 1
        number_of_colored_cells= 0
        # i = 1
        while(colored_rows<row_count):
            number_of_colored_cells+=colored_rows
            colored_rows+=2
            # i+=1
        return number_of_colored_cells*2+row_count


