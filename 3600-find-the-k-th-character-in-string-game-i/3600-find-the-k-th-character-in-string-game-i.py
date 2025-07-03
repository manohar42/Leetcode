class Solution:
    def kthCharacter(self, k: int) -> str:
        
        s= ""
        word = "a"
        for i in range(0,k):
            char = ""
            n = len(word)
            j = 0
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