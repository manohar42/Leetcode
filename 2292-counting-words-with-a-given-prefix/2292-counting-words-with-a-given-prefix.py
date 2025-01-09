class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        for i in range(0,len(words)):
            if words[i].startswith(pref):
                count+=1
        return count