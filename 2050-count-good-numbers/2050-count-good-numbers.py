class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10**9+7
        if n%2==0:
            return ((5**(n//2))*(4**(n//2)))%mod
        else:
            return ((5**(n//2+1))*(4**(n//2)))%mod