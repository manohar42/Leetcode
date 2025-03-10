class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        charList = set()
        count = 0
        for i in range(0,len(word)):
            charList = set()
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    charList.add(word[j])
                else:
                    break
                if len(charList) ==5:
                    count+=1
        return count
