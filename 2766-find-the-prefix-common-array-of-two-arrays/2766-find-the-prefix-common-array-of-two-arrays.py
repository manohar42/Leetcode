class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        hashmap = {}
        n = len(A)
        count = 0
        res = []
        for i in range(0,n):
            hashmap[A[i]] = hashmap.get(A[i],0)+1
            hashmap[B[i]] = hashmap.get(B[i],0)+1
            if A[i] != B[i]:
                if hashmap[A[i]] == 2:
                    count+=1
                if hashmap[B[i]] == 2:
                    count+=1
            else:
                if hashmap[A[i]] == 2:
                    count+=1
            res.append(count)
        return res
                