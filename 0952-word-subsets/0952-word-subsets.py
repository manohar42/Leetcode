class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def word_count_1(word):
            hashmap ={}
            for i in word:
                hashmap[i]= hashmap.get(i,0)+1
            return hashmap
        hashmap ={}
        char_count = {}
        for i in words2:
            for ch in i:
                char_count[ch] = char_count.get(ch,0)+1
            for j in char_count:
                hashmap[j] = max(char_count[j],hashmap.get(j,0))
                char_count[j] = 0
        res = []
        for word in words1:
            hashmap_words1 = word_count_1(word)
            subset = True
            for i in hashmap:
                if hashmap[i] <= hashmap_words1.get(i,0):
                    continue
                else:
                    subset = False
            if subset:
                res.append(word)
        return res
