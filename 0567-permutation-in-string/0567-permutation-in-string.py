class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        left = 0
        right=0
        n = len(s1)
        m = len(s2)
        count = [0]*26
        window_frequency = [0]*26
        if n>m:
            return False
        
        for i in range(0,n):
            count[ord(s1[i])-ord('a')] +=1
            window_frequency[ord(s2[i])-ord('a')] +=1
        
        if count == window_frequency:
            return True
        
        for i in range(n,m):
            window_frequency[ord(s2[i-n])-ord('a')] -=1
            window_frequency[ord(s2[i])-ord('a')] +=1

            if window_frequency == count:
                return True
        return False