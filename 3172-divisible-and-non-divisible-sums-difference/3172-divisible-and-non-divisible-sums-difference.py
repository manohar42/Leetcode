class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        sum_value = (n*(n+1))//2
        print(sum_value)

        for i in range(1,n+1):
            if i%m == 0:
                sum_value-= (2*i)
                # print(sum_value)
        return sum_value