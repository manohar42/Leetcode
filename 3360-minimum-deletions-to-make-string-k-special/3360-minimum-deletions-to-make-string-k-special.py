class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        s = [0 for i in range(0,26)]
        for i in word:
            s[ord(i)-ord('a')] +=1
        c_count = 0
        s.sort()
        min_count = len(word)
        for i in range(0,26): 
            min_val = s[i]
            if s[i] > 0:
                c_count =0
                for j in range(0,26):
                    if s[j]!=0 and i!=j:
                        if s[j] < min_val:
                            c_count+=s[j]
                        elif s[j]-min_val <=k:
                            continue
                        else:
                            c_count+=s[j]-min_val-k
                if c_count < min_count:
                    min_count = c_count
        return min_count
                


