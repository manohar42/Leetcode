class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

    
        
        a = abs(dividend)
        b = abs(divisor)
    
        if (dividend<0 and divisor >=0) or (divisor<0 and dividend >= 0):
            sign = -1
        else:
            sign = 1
       
        q = len(range(0,a-b+1,b))
        minus_limit = (-(2**31)-1)
        # print(minus_limit)
        plus_limit = (2**31-1)
        return min(max(minus_limit,q*sign),plus_limit)
