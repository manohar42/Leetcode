class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        sum_value = (n*(n+1))//2
    
        value = 0
        res = 0
        while res+m <= n:
            res +=m
            value+=res
        return sum_value - (2*value)