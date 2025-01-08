class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1,str2):
            
            k = len(str1)
            m = len(str2)
            if str1 == str2[:k] and str1 == str2[m-k:]:
                return 1
            return 0
        
        n = len(words)
        count = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if len(words[i]) <= len(words[j]):
                    count+=isPrefixAndSuffix(words[i],words[j])
        return count