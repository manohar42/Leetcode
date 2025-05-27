class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        sum_value = (n*(n+1))//2
    
        for i in range(1,n+1):
            if i%m == 0:
                sum_value-= (2*i)
        return sum_value