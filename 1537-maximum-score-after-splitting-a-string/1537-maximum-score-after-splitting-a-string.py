class Solution:
    def maxScore(self, s: str) -> int:
        
        zero_count = 0
        one_count = 0

        for i in s:
            if i == '0':
                zero_count+=1
            else:
                one_count+=1
        
        count = 0
        zeros = 0
        ones = 0
        n = len(s)
        for i in range(0,n-1):
            if s[i] == '0':
                zeros+=1
            ones = n-1-i-zero_count+zeros
            # print(zeros,ones)
            count = max(zeros+ones, count)
        return count