class Solution:
    def myPow(self, x: float, n: int) -> float:

        def Ppow(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = Ppow(x,n//2)
            res = res*res

            if n%2 == 1:
                res=res*x
            return res
        
        if n>0:
            return Ppow(x,abs(n))
        else:
            return 1/Ppow(x,abs(n))
