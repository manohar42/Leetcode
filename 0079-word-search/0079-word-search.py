class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:   
        def dfs(i,j,value,visited):
            if value == len(word):
                    return True
            if i < 0 or i > row-1 or j < 0 or j > column-1:
                return False
            else:
                # print(visited,i,j)
                if board[i][j] == word[value] and visited[i][j] == False:
                    # print(i,j)
                    visited[i][j] = True
                    if dfs(i+1,j,value+1,visited) or dfs(i-1,j,value+1,visited) or dfs(i,j+1,value+1,visited) or dfs(i,j-1,value+1,visited):
                        return True
                    else:
                        visited[i][j] = False
            visited[i][j] == False
            return False
                
                

                
        row = len(board)
        column = len(board[0])
        visit = [[False for _ in range(0,column+1)] for _ in range(0,row+1)]
        for i in range(0,row):
            for j in range(0,column):
                # print(board[i][j])
                if board[i][j] == word[0]:
                    # print(visit)
                    if dfs(i,j,0,visit):
                        # print("Word Found")
                        return True

        return False
