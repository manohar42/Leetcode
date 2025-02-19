class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabets = ['a','b','c']
        resultset = []
        def sets(n,s):
            if len(resultset) == k:
                    return
                    
            if len(s) == n:
                resultset.append(s[:])
                return
            for i in alphabets:
                if len(s) == 0:
                    sets(n,i)
                else:
                    if s[-1]!= i:
                        sets(n,s+i)
        
        sets(n,'')
        if k > len(resultset):
            return ""
        return resultset[k-1]