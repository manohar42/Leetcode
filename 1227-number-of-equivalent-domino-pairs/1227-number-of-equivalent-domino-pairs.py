class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        n = len(dominoes)
        hashmap = {}
        for i in range(0,n):
            dominoes[i].sort()
            # print(dominoes[i][0],dominoes[i][1])
            hashmap[(dominoes[i][0],dominoes[i][1])] = hashmap.get((dominoes[i][0],dominoes[i][1]),0)+1
        count = 0
        for i in hashmap:
            if hashmap[i] > 1:
                count+=(hashmap[i]*(hashmap[i]-1))//2
        return count