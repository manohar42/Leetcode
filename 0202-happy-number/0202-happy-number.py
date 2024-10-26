class Solution:
    def isHappy(self, n: int) -> bool:
        numList = []
        sum_value = 0
        num_value = n
        while sum_value != 1:
            sum_value = 0
            while num_value > 0:
                k = num_value%10
                sum_value+= k*k
                num_value = num_value//10
            if sum_value in numList:
                return False
            numList.append(sum_value)
            num_value = sum_value 
            # print(numList)
        return True
            
