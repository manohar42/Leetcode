class Solution:
    def maxDifference(self, s: str) -> int:
        n = len(s)
        min_freq = n
        max_freq = 0
        lis = [0]*26
        for i in range(0,n):
            lis[ord(s[i])-97]+=1
        for i in lis:
            if i%2!=0 and i > max_freq:
                max_freq = i
            if i%2 == 0 and i < min_freq and i!=0:
                min_freq = i
        print(max_freq,min_freq)
        return max_freq-min_freq 