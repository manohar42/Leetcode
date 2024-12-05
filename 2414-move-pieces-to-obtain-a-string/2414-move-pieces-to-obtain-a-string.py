class Solution:
    def canChange(self, start: str, target: str) -> bool:
        

        n = len(start)
        m = len(target)
        if n != m or start.count('L') != target.count('L') or start.count('R') != target.count('R'):
            return False
        
        
        i = 0
        j = 0
        while i < n and j < m:
            while i<n and start[i] == "_":
                i+=1
            while j < m and target[j] == "_":
                j+=1
            # print(i,j)
            if i<n and j<m:
                if (start[i] == 'L' and target[j] == 'L' and i >= j) or (start[i] == 'R' and target[j] == 'R' and i <= j):
                    i+=1
                    j+=1
                    continue
                else:
                    # print("For L",start,target,i,j)
                    return False
            
        return True
