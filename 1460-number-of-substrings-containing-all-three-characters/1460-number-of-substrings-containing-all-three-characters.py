class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        freq = [0]*3

        right = 0
        left = 0
        total = 0
        n = len(s)

        while right < n:
            freq[ord(s[right])-ord('a')]+=1
            while(freq[0]>0 and freq[1]>0 and freq[2]>0):

                total += n-right
                freq[ord(s[left])-ord('a')]-=1
                left+=1
            right+=1
        return total