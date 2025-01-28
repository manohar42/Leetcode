class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False
        char = [0 for _ in range(0,26)]
        n = len(s)
        for i in range(n):
            char[ord(s[i]) - ord('a')] +=1
            char[ord(t[i]) - ord('a')] -=1
        for j in char:
            if j != 0:
                return False
        return True