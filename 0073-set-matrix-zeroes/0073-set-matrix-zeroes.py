class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zeros = []
        col_zeros = []
        for row in range(0,m):
            for col in range(0,n):
                if matrix[row][col] == 0:
                    row_zeros.append(row)
                    col_zeros.append(col)
        for i in row_zeros:
            for j in range(0,n):
                matrix[i][j] = 0
        for i in col_zeros:
            for j in range(0,m):
                matrix[j][i] = 0
        return matrix

