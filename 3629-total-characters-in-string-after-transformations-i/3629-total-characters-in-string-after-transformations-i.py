class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        mod = (10**9)+7
        hashmap = [0]*26
        for i in s:
            hashmap[ord(i)-ord('a')] +=1       
        
        for i in range(0,t):    
            NewMap = hashmap.copy()
            for j in range(0,26):
                if hashmap[j] > 0:
                    NewMap[j]-=hashmap[j]
                    if (j+1)%26 == 0:
                        NewMap[0]+=hashmap[j]
                        NewMap[1]+=hashmap[j]
                    else:
                        NewMap[j+1] +=hashmap[j]
        
            hashmap = NewMap.copy()
        
        res = 0
        
        return sum(hashmap)%mod    