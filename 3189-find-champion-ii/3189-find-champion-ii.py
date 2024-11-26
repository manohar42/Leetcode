class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        hashmap = [False]*n
        count = 0 
        for i in edges:
            if hashmap[i[1]] == False:
                count+=1
            hashmap[i[1]]+=1
        if count < n-1:
            return -1
        for i in range(n):
            if hashmap[i] == False:
                return i
            
        
