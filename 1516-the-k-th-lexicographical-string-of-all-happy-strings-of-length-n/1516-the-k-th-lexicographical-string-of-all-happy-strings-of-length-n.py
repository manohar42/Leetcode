class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabets = ['a','b','c']

        resultset = []
        def sets(n,s):
            # print(s)
            if len(s) == n:
                resultset.append(s[:])
                return
            for i in alphabets:
                # print("s,i",s,i)
                if len(s) == 0:
                    sets(n,i)
                else:
                    # print("s[-1],i",s[-1],i)
                    if s[-1]!= i:
                        sets(n,s+i)
        
        sets(n,'')
        # print(resultset)
        if k > len(resultset):
            return ""
        return resultset[k-1]