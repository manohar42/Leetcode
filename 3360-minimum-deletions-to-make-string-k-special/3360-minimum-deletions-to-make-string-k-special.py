class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        s = [0 for i in range(0,26)]
        for i in word:
            s[ord(i)-ord('a')] +=1
        c_count = 0
        s.sort()
        prefix_sum = 0
        min_count = len(word)
        for i in range(0,26): 
            min_val = s[i]
            prefix_sum+=s[i-1] if i > 0 else 0
            if s[i] > 0:
                c_count = prefix_sum
                for j in range(i+1,26):
                    if s[j] < min_val:
                        c_count+=s[j]
                    elif s[j]-min_val <=k:
                        continue
                    else:
                        c_count+=s[j]-min_val-k
                if c_count < min_count:
                    min_count = c_count
        return min_count
                


