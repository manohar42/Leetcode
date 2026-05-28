class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       

        count = 0

        hashmap = {}

        for i in range(0,len(word)):

            if ord(word[i]) in hashmap:
                hashmap[ord(word[i])][1] = i
            else:
                hashmap[ord(word[i])] = [i,i]
        # print(hashmap)
        for i in hashmap:
            
            if i <=90 and i+32 in hashmap and hashmap[i][0] > hashmap[i+32][1]:
                count+=1
                # print(ord(word[i]))
               

        return count