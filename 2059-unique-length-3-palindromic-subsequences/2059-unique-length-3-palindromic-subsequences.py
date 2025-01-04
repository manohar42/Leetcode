class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        hashmap = defaultdict(list)
        set_s = set(s)
        count = 0
        for i in set_s:
            start = s.find(i)
            end = s.rfind(i)

            if start != end:
                
                count+= len(set(s[start+1:end]))
        return count
            

            
