class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        hashmap = {}
        for i in words:
            hashmap[i] = 0
            hashmap[i[::-1]] = 0
        res = 0
        for i in words:
            if hashmap[i[::-1]] > 0:
                res+=4
                hashmap[i[::-1]]-=1
                # print(res,i)
            else:
                hashmap[i]+=1
            
        for i in hashmap:
            if i[0] == i[1] and hashmap[i] > 0:
                res+=2
                break
        return res
            


