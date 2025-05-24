class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        res = []
        for i in range(0,len(words)):
            # s = set(words[i])
            if x in words[i]:
                res.append(i)
        
        return res
                    