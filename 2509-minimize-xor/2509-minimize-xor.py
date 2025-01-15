class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        a, b = bin(num1).count('1'), bin(num2).count('1')
        result = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                result ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                result ^= 1 << i
                a += 1
        return result