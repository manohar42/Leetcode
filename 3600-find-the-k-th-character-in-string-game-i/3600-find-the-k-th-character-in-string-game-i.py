class Solution:
    def kthCharacter(self, k: int) -> str:
        
        char= ""
        word = "a"
        j = 0
        while len(word) < k:
            n = len(word)
            while j < n:
                if ord(word[j])+1 > 122:
                    char+="a"
                else:
                    char+=chr(ord(word[j])+1)

                j+=1
            word+=char
            
        return word[k-1]