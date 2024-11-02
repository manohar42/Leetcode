class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == " " or len(s) == 1:
            return 1

        slow = 0
        fast = 0
        hashmap={}
        max_length = 0
        count = 0
        while slow < len(s) and fast < len(s):
            if hashmap.get(s[fast],-1) == -1:
                # print("Fast", s[fast])
                hashmap[s[fast]] = fast
                count+=1
                # print("CurrentSize", count)
                fast+=1  
            else:
                # print("Slow")
                if slow <= hashmap[s[fast]]:
                    slow = hashmap[s[fast]]+1
                    
                    del hashmap[s[fast]]
                    max_length = max(max_length, count)
                    count = fast - slow
                    # print("CurrentSize", count, slow)
                else:
                    del hashmap[s[fast]]

            # print(fast)
            
        return max(max_length,count)