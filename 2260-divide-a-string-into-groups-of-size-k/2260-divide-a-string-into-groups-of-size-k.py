class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        p = ""
        for i in s:
            p+=i
            if len(p) == k:
                res.append(p)
                p = ""
        if len(p) < k and p!="":
            p+=fill*(k-len(p))
            res.append(p)
        return res
