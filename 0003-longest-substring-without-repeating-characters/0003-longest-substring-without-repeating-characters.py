class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        count = 0
        left = 0
        for right,c in enumerate(s):

            if c in hashmap and hashmap[c] >= left:
                left=hashmap[c]+1
            hashmap[c] =  right
            # print(hashmap)
            count = max(count,right-left+1)
        return count
