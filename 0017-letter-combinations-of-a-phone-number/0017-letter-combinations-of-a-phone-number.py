class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = []

        hashmap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}


        def backtrack(digits,n,i,arr):
            if i == n:
                res.append("".join(arr[:]))
                return
            for j in hashmap[digits[i]]:
                arr.append(j)
                backtrack(digits,n,i+1,arr)
                arr.pop()
        
        backtrack(digits,len(digits),0,[])
        return res