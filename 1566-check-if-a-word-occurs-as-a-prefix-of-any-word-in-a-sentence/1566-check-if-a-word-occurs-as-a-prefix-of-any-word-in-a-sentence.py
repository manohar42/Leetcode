class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        lis = sentence.split()
        print(lis)
        k = len(searchWord)
        for i in range(len(lis)):
            if len(lis[i]) >= k and searchWord == lis[i][:k]:
                return i+1
        return -1