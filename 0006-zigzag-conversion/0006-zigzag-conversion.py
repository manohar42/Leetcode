class Solution:
    def convert(self, s: str, numRows: int) -> str:

        k = len(s)//numRows
        if numRows == 1:
            return s
        # print(k)
        
        matrix = [["" for i in range(0,len(s))] for i in range(0,numRows)]
        # print(matrix)
        row = 0
        col = 0
        for i in range(0,len(s)):
            insert =False
            while insert == False:
                if col == 0 or (col)%(numRows-1) == 0 :
                    # print(row,col,s[i],i)
                    matrix[row][col] +=s[i]
                    insert = True
                    row+=1
                else:
                    # print(row,col)
                    row = numRows-(col%(numRows-1))-1
                    
                    matrix[row][col] = s[i]
                    insert = True
                    col+=1
                    row = 0
                if row == numRows:
                    row = 0
                    col+=1
                
        output = ""
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[0])):
                output+=matrix[row][col]
        return output