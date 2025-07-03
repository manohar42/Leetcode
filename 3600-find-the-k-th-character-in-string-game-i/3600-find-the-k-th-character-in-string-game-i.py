class Solution:
    def kthCharacter(self, k: int) -> str:
        
        char= ""
        word = "a"
        j = 0
        for i in range(0,k):
            n = len(word)
            while j < n:
                s=ord(word[j])+1
                if s > 122:
                    s= 97
                char+=chr(s)
                j+=1
            word+=char
            if len(word) > k:
                break
            
        return word[k-1]