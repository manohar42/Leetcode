class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(l,n,k,arr):
            
            if len(arr) == k:
                res.append(arr[:])
                return
            if l == n:
                return
            arr.append(l+1)
            backtrack(l+1,n,k,arr)
            arr.pop()
            backtrack(l+1,n,k,arr)
            
        
        backtrack(0,n,k,[])
        return res