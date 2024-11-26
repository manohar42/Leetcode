class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        hashmap = defaultdict()
        for i in range(n):
            hashmap[i] = 0
        count = 0 
        for i in edges:
            if hashmap[i[1]] == 0:
                count+=1
            hashmap[i[1]]+=1
        if count < n-1:
            return -1
        for i in hashmap:
            if hashmap[i] == 0:
                return i
            
        
