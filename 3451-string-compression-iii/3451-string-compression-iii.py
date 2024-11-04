class Solution:
    def compressedString(self, word: str) -> str:
        
        s = ""
        n = len(word)
        count = 1
        for i in range(1,n):
            if i > 0:
                if word[i] == word[i-1]:
                    count+=1
                else:
                    s+=str(count)+word[i-1]
                    count = 1
            if count > 9:
                s+=str(count-1)+word[i-1]
                count = count-9
        s+=str(count)+word[-1]
        return s
