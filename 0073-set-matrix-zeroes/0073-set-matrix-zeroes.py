class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zeros = set()
        col_zeros = set()
        for row in range(0,m):
            for col in range(0,n):
                if matrix[row][col] == 0:
                    row_zeros.add(row)
                    col_zeros.add(col)
        for i in row_zeros:
            for j in range(0,n):
                matrix[i][j] = 0
        for i in col_zeros:
            for j in range(0,m):
                matrix[j][i] = 0
        return matrix

