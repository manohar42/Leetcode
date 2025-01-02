class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = ['a','e','i','o','u']
        n = len(words)

        hashmap = {}
        count = 0
        for i in range(0,n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count+=1
            hashmap[i] = count 
            
        ans = []
        for i,j in queries:
            count = hashmap[j] - hashmap[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                count+=1
            ans.append(count)
        return ans